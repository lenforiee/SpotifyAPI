from __future__ import annotations

from typing import Optional
from typing import TypeVar
from typing import Generic

from pydantic import BaseModel

T = TypeVar("T")


class GenericList(BaseModel, Generic[T]):
    href: str
    limit: int
    next: Optional[str] = None
    offset: int
    previous: Optional[str] = None
    total: int
    items: list[T]


class ExternalUrls(BaseModel):
    spotify: str


class Image(BaseModel):
    url: str
    height: Optional[int] = None
    width: Optional[int] = None


class Copyright(BaseModel):
    text: str
    type: str


class Restrictions(BaseModel):
    reason: str


class ResumePoint(BaseModel):
    fully_played: bool
    resume_position_ms: int


class ExternalIds(BaseModel):
    isrc: str
    ean: str
    upc: str
