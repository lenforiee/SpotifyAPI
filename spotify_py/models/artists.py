from __future__ import annotations

from pydantic import BaseModel
from typing import Literal

from .shared.image import Image
from .shared.external_urls import ExternalUrls
from .shared.followers import Followers


class SimplifiedArtist(BaseModel):
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: Literal["artist"]
    uri: str


class Artist(SimplifiedArtist):
    followers: Followers
    genres: list[str]
    images: list[Image]
    popularity: int
