from __future__ import annotations

from pydantic import BaseModel
from spotify_py.models.base import Image


class Category(BaseModel):
    href: str
    icons: list[Image]
    id: str
    name: str
