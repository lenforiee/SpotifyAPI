from __future__ import annotations

from pydantic import BaseModel


class ExternalUrls(BaseModel):
    spotify: str
