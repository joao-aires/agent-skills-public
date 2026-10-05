"use client";
import { FormEvent, useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";

import type { components } from "@/lib/api-schema";
type Note = components["schemas"]["NoteOutput"];
async function api(path: string, data?: unknown) {
  const response = await fetch(`/api/${path}`, data === undefined ? {} : {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data),
  });
  if (!response.ok) throw new Error(response.status === 401 ? "Sign in required or invalid credentials." : "Request failed. Check your input and try again.");
  return response.status === 204 ? null : response.json();
}
export default function Page() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState<string | null>(null);
  const [notes, setNotes] = useState<Note[]>([]);
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const [loading, setLoading] = useState(true);
  async function refresh() { setNotes(await api("notes")); }
  useEffect(() => { api("me").then(async (u) => { setUser(u.email); setNotes(await api("notes")); }).catch((e) => { if (!e.message.includes("Sign in required")) setError("Could not load your workspace. Try again shortly."); }).finally(() => setLoading(false)); }, []);
  async function authenticate(event: FormEvent<HTMLFormElement>, register = false) {
    event.preventDefault(); setBusy(true); setError("");
    try { const u = await api(`auth/${register ? "register" : "login"}`, { email, password }); setUser(u.email); setPassword(""); await refresh(); }
    catch (e) { setError((e as Error).message); } finally { setBusy(false); }
  }
  async function create(event: FormEvent) {
    event.preventDefault(); setBusy(true); setError("");
    try { await api("notes", { title }); setTitle(""); await refresh(); }
    catch (e) { setError((e as Error).message); } finally { setBusy(false); }
  }
  return <main className="min-h-screen bg-background text-foreground px-4 py-12"><div className="mx-auto max-w-xl space-y-6">
    <header><p className="text-sm text-muted-foreground">Full-stack reference</p><h1 className="text-3xl font-semibold tracking-tight">Project Notes</h1></header>
    {loading ? <p role="status">Loading your workspace…</p> : user ? <>
      <div className="flex items-center justify-between gap-4"><p className="text-sm truncate">{user}</p><Button variant="outline" disabled={busy} onClick={async () => {
        setBusy(true); setError(""); try { await api("auth/logout", {}); setUser(null); setNotes([]); } catch (e) { setError((e as Error).message); } finally { setBusy(false); }
      }}>Sign out</Button></div>
      <Card><CardHeader><CardTitle>Capture a note</CardTitle><CardDescription>Notes stay private to your account.</CardDescription></CardHeader><CardContent>
        <form onSubmit={create} className="space-y-3"><Label htmlFor="title">Note title</Label><Input id="title" value={title} onChange={(e) => setTitle(e.target.value)} required maxLength={120} /><Button disabled={busy || !title.trim()}>Save note</Button></form>
      </CardContent></Card>
      <section aria-label="Saved notes"><h2 className="mb-3 text-lg font-medium">Your notes</h2>{notes.length ? <ul className="space-y-2">{notes.map(n => <li key={n.id} className="rounded-lg border bg-card p-4">{n.title}</li>)}</ul> : <p className="text-muted-foreground">No notes yet. Capture your first idea above.</p>}</section>
    </> : <Card><CardHeader><CardTitle>Your workspace</CardTitle><CardDescription>Sign in or create an account to save your notes.</CardDescription></CardHeader><CardContent>
      <form className="space-y-4" onSubmit={(e) => { const action = (e.nativeEvent as SubmitEvent).submitter?.getAttribute("value"); void authenticate(e, action === "register"); }}>
        <div className="space-y-2"><Label htmlFor="email">Email</Label><Input id="email" type="email" autoComplete="email" value={email} onChange={e => setEmail(e.target.value)} required /></div>
        <div className="space-y-2"><Label htmlFor="password">Password</Label><Input id="password" type="password" autoComplete="current-password" minLength={12} maxLength={128} value={password} onChange={e => setPassword(e.target.value)} required /><p className="text-sm text-muted-foreground">At least 12 characters.</p></div>
        <div className="flex flex-wrap gap-2"><Button name="action" value="login" disabled={busy}>Sign in</Button><Button variant="outline" name="action" value="register" disabled={busy}>Create account</Button></div>
      </form>
    </CardContent></Card>}
    {error && <p role="alert" className="text-destructive">{error}</p>}
  </div></main>;
}
