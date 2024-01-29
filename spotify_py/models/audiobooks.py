from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from spotify_py.models.base import ExternalUrls
from spotify_py.models.base import Image
from spotify_py.models.base import Copyright
from spotify_py.models.base import GenericList
from spotify_py.models.base import Restrictions
from spotify_py.models.base import ResumePoint


class SimplifiedChapter(BaseModel):
    audio_preview_url: Optional[str] = None
    available_markets: Optional[list[str]] = None
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
    release_date_precision: str
    resume_point: ResumePoint
    type: str
    uri: str
    restrictions: Optional[Restrictions] = None


class Chapter(SimplifiedChapter):
    audiobook: SimplifiedAudiobook


class AudiobookCredit(BaseModel):
    name: str


class SimplifiedAudiobook(BaseModel):
    authors: list[AudiobookCredit]
    available_markets: list[str]
    copyrights: list[Copyright]
    description: str
    html_description: str
    edition: Optional[str] = None
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    languages: list[str]
    media_type: str
    name: str
    narrators: list[AudiobookCredit]
    publisher: str
    type: str
    uri: str
    total_chapters: int


class Audiobook(SimplifiedAudiobook):
    chapters: GenericList[SimplifiedChapter]
