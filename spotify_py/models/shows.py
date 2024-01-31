from __future__ import annotations

from typing import Literal
from typing import TYPE_CHECKING

from pydantic import BaseModel

from .shared.external_urls import ExternalUrls
from .shared.image import Image
from .shared.copyright import Copyright
from .shared.paging_object import PagingObject

if TYPE_CHECKING:  # avoid circular imports
    from .episodes import SimplifiedEpisode


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
    type: Literal["show"]
    uri: str
    total_chapters: int


class Show(SimplifiedShow):
    episodes: PagingObject[SimplifiedEpisode]
