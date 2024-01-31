from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel

from .episodes import Episode
from .shared.external_urls import ExternalUrls
from .shared.followers import Followers
from .shared.image import Image
from .shared.paging_object import PagingObject
from .tracks import Track
from .users import UserBase


class PlaylistTrack(BaseModel):
    added_at: Optional[datetime] = None
    added_by: Optional[UserBase] = None
    is_local: bool
    track: Union[Track, Episode]


class SimplifiedPlaylist(BaseModel):
    collaborative: bool
    description: Optional[str] = None
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    name: str
    owner: UserBase
    public: Optional[bool] = None
    snapshot_id: str
    tracks: PagingObject[Track]
    type: Literal["playlist"]
    uri: str


class Playlist(SimplifiedPlaylist):
    followers: Followers
