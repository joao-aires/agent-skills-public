from pydantic import BaseModel, Field


class IdeaSummary(BaseModel):
    summary: str = Field(min_length=1, max_length=240)
    tags: list[str] = Field(max_length=5)


def validate_summary(raw: str) -> IdeaSummary:
    return IdeaSummary.model_validate_json(raw)
