from __future__ import annotations

from pydantic import BaseModel


class Copyright(BaseModel):
    text: str
    type: str
