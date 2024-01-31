from __future__ import annotations

from pydantic import BaseModel


class ResumePoint(BaseModel):
    fully_played: bool
    resume_position_ms: int
