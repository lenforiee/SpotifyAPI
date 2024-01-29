from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from spotify_py.models.base import ExternalUrls
from spotify_py.models.base import Image
from spotify_py.models.base import Copyright
from spotify_py.models.base import GenericList
from spotify_py.models.base import Restrictions
from spotify_py.models.base import ResumePoint


class SimplifiedEpisode(BaseModel):
    audio_preview_url: Optional[str] = None
    description: str
    html_description: str
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    is_externally_hosted: bool
    is_playable: bool
    languages: list[str]
    name: str
    release_date: str
    release_date_precision: str
    resume_point: ResumePoint
    type: str
    uri: str
    restrictions: Optional[Restrictions] = None


class Episode(SimplifiedEpisode):
    show: SimplifiedShow


class SimplifiedShow(BaseModel):
    available_markets: list[str]
    copyrights: list[Copyright]
    description: str
    html_description: str
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    is_externally_hosted: bool
    languages: list[str]
    media_type: str
    name: str
    publisher: str
    type: str
    uri: str
    total_chapters: int


class Show(SimplifiedShow):
    episodes: GenericList[SimplifiedEpisode]
