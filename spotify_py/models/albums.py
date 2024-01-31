from __future__ import annotations

from typing import Optional
from typing import Literal
from typing import TYPE_CHECKING
from pydantic import BaseModel

from .artists import SimplifiedArtist

from .shared.external_urls import ExternalUrls
from .shared.restrictions import Restrictions
from .shared.external_ids import ExternalIds
from .shared.image import Image
from .shared.paging_object import PagingObject
from .shared.copyright import Copyright

if TYPE_CHECKING:  # avoid circular imports
    from .tracks import SimplifiedTrack


class SimplifiedAlbum(BaseModel):
    album_type: Literal["album", "single", "compilation"]
    total_tracks: int
    available_markets: list[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    name: str
    release_date: str
    release_date_precision: Literal["year", "month", "day"]
    restrictions: Optional[Restrictions] = None
    type: Literal["album"]
    uri: str
    artists: list[SimplifiedArtist]


class Album(BaseModel):
    tracks: PagingObject[SimplifiedTrack]
    copyrights: list[Copyright]
    external_ids: ExternalIds
    genres: list[str]
    label: str
    popularity: int
