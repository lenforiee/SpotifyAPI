from __future__ import annotations

from typing import Optional
from typing import Literal
from typing import TYPE_CHECKING
from pydantic import BaseModel

from .artists import SimplifiedArtist
from .shared.external_urls import ExternalUrls
from .shared.restrictions import Restrictions
from .shared.external_ids import ExternalIds

if TYPE_CHECKING:  # avoid circular imports
    from .albums import SimplifiedAlbum


class TrackLinkedFrom(BaseModel):
    external_urls: ExternalUrls
    href: str
    id: str
    type: Literal["track"]
    uri: str


class SimplifiedTrack(BaseModel):
    artists: list[SimplifiedArtist]
    available_markets: list[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    is_playable: bool
    linked_from: Optional[TrackLinkedFrom] = None
    restrictions: Optional[Restrictions] = None
    name: str
    preview_url: Optional[str] = None
    track_number: int
    type: Literal["track"]
    uri: str
    is_local: bool


class Track(SimplifiedTrack):
    album: SimplifiedAlbum
    external_ids: ExternalIds
    popularity: int
