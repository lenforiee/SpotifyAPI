from __future__ import annotations

from typing import Optional
from typing import TypeVar
from typing import Generic

from pydantic import BaseModel

T = TypeVar("T")


class PagingObject(BaseModel, Generic[T]):
    href: str
    limit: int
    next: Optional[str] = None
    offset: int
    previous: Optional[str] = None
    total: int
    items: list[T]


class Cursor(BaseModel):
    after: str
    before: str


class CursorPagingObject(BaseModel, Generic[T]):
    href: str
    limit: int
    next: Optional[str] = None
    cursors: Cursor
    total: int
    items: list[T]
