from __future__ import annotations

from pydantic import BaseModel


class ExternalIds(BaseModel):
    isrc: str
    ean: str
    upc: str
