from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from spotify_py.models.base import Image
from spotify_py.models.base import ExternalUrls


class SimplifiedArtist(BaseModel):
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str


class ArtistFollowers(BaseModel):
    href: Optional[str] = None
    total: int


class Artist(SimplifiedArtist):
    followers: ArtistFollowers
    genres: list[str]
    images: list[Image]
    popularity: int
