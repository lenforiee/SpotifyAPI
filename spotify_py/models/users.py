from __future__ import annotations

from typing import Literal
from typing import Optional

from pydantic import BaseModel

from .shared.external_urls import ExternalUrls
from .shared.followers import Followers
from .shared.image import Image


class UserBase(BaseModel):
    display_name: Optional[str] = None
    external_urls: ExternalUrls
    followers: Followers
    href: str
    id: str
    type: Literal["user"]
    uri: str


class UserPublic(UserBase):
    images: list[Image]


class UserExplicitContent(BaseModel):
    filter_enabled: bool
    filter_locked: bool


class UserPrivate(UserPublic):
    country: str
    email: str
    explicit_content: UserExplicitContent
    product: Literal["premium", "free", "open"]
