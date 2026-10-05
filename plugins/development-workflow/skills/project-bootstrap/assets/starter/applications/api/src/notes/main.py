import hashlib
import os
import secrets
from datetime import UTC, datetime, timedelta
from typing import Annotated
from uuid import UUID

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from pwdlib import PasswordHash
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from sqlalchemy import select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .db import session
from .models import LoginSession, Note, User

app = FastAPI(title="Project Notes", version="0.1.0")
passwords = PasswordHash.recommended()
DUMMY_HASH = passwords.hash(secrets.token_urlsafe(32))
DB = Annotated[Session, Depends(session)]
ORIGIN = os.environ.get("WEB_ORIGIN", "http://localhost:3000")
COOKIE_SETTING = os.environ.get("COOKIE_SECURE", "true")
if COOKIE_SETTING not in {"true", "false"}:
    raise RuntimeError("COOKIE_SECURE must explicitly be true or false")
SECURE = COOKIE_SETTING == "true"


class Credentials(BaseModel):
    email: EmailStr
    password: str = Field(min_length=12, max_length=128)


class NoteInput(BaseModel):
    title: str = Field(min_length=1, max_length=120)

    @field_validator("title")
    @classmethod
    def clean_title(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Title cannot be blank")
        return value


class NoteOutput(NoteInput):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    created_at: datetime


class UserOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    email: str


@app.middleware("http")
async def csrf(request: Request, call_next):
    if request.method not in {"GET", "HEAD", "OPTIONS"} and request.headers.get("origin") != ORIGIN:
        from fastapi.responses import JSONResponse

        return JSONResponse({"detail": "Untrusted or missing origin"}, status_code=403)
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    return response


def current_user(request: Request, db: DB) -> User:
    token = request.cookies.get("session")
    login = db.get(LoginSession, hashlib.sha256(token.encode()).hexdigest()) if token else None
    if login is None or login.expires_at <= datetime.now(UTC):
        raise HTTPException(401, "Sign in required")
    user = db.get(User, login.user_id)
    if user is None:
        raise HTTPException(401, "Sign in required")
    return user


Auth = Annotated[User, Depends(current_user)]


def sign_in(user: User, db: Session, response: Response):
    token = secrets.token_urlsafe(32)
    db.add(
        LoginSession(
            token_hash=hashlib.sha256(token.encode()).hexdigest(),
            user_id=user.id,
            expires_at=datetime.now(UTC) + timedelta(hours=12),
        )
    )
    db.commit()
    response.set_cookie(
        "session", token, httponly=True, secure=SECURE, samesite="lax", max_age=43200, path="/"
    )


@app.get("/api/health")
def health(db: DB):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}


@app.post("/api/auth/register", response_model=UserOutput, status_code=201)
def register(data: Credentials, response: Response, db: DB):
    user = User(email=str(data.email).lower(), password_hash=passwords.hash(data.password))
    db.add(user)
    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        raise HTTPException(409, "Account cannot be created") from None
    sign_in(user, db, response)
    return user


@app.post("/api/auth/login", response_model=UserOutput)
def login(data: Credentials, response: Response, db: DB):
    user = db.scalar(select(User).where(User.email == str(data.email).lower()))
    valid = passwords.verify(data.password, user.password_hash if user else DUMMY_HASH)
    if user is None or not valid:
        raise HTTPException(401, "Invalid credentials")
    sign_in(user, db, response)
    return user


@app.post("/api/auth/logout", status_code=204)
def logout(request: Request, response: Response, db: DB, user: Auth):
    token = request.cookies["session"]
    item = db.get(LoginSession, hashlib.sha256(token.encode()).hexdigest())
    if item:
        db.delete(item)
        db.commit()
    response.delete_cookie("session", path="/", secure=SECURE, httponly=True, samesite="lax")


@app.get("/api/me", response_model=UserOutput)
def me(user: Auth):
    return user


@app.get("/api/notes", response_model=list[NoteOutput])
def list_notes(db: DB, user: Auth):
    return list(db.scalars(select(Note).where(Note.owner_id == user.id).order_by(Note.created_at)))


@app.post("/api/notes", response_model=NoteOutput, status_code=201)
def add_note(data: NoteInput, db: DB, user: Auth):
    note = Note(owner_id=user.id, title=data.title)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@app.get("/api/notes/{note_id}", response_model=NoteOutput)
def get_note(note_id: UUID, db: DB, user: Auth):
    note = db.scalar(select(Note).where(Note.id == note_id, Note.owner_id == user.id))
    if note is None:
        raise HTTPException(404, "Note not found")
    return note
