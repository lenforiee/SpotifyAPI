from __future__ import annotations

from typing import Optional
from typing import Literal
from typing import TYPE_CHECKING

from pydantic import BaseModel

from .shared.external_urls import ExternalUrls
from .shared.image import Image
from .shared.resume_point import ResumePoint
from .shared.restrictions import Restrictions

if TYPE_CHECKING:  # avoid circular imports
    from .audiobooks import SimplifiedAudiobook


class SimplifiedChapter(BaseModel):
    audio_preview_url: Optional[str] = None
    available_markets: list[str]
    chapter_number: int
    description: str
    html_description: str
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    is_playable: bool
    languages: list[str]
    name: str
    release_date: str
    release_date_precision: Literal["year", "month", "day"]
    resume_point: ResumePoint
    type: Literal["episode"]  # XXX: documentation says episode for some reason
    uri: str
    restrictions: Optional[Restrictions] = None


class Chapter(SimplifiedChapter):
    audiobook: SimplifiedAudiobook
