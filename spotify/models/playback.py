from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel

from .devices import Device
from .episodes import Episode
from .shared.external_urls import ExternalUrls
from .tracks import Track


# Since all variables are optional, lets initialise them with false
class PlaybackActions(BaseModel):
    interrupting_playback: bool = False
    pausing: bool = False
    resuming: bool = False
    seeking: bool = False
    skipping_next: bool = False
    skipping_prev: bool = False
    toggling_repeat_context: bool = False
    toggling_shuffle: bool = False
    toggling_repeat_track: bool = False
    transferring_playback: bool = False


class PlaybackContext(BaseModel):
    type: str  # TODO: add literal types here
    href: str
    external_urls: ExternalUrls
    uri: str


class PlaybackState(BaseModel):
    device: Device
    repeat_state: Literal["off", "track", "context"]
    shuffle_state: bool
    context: Optional[PlaybackContext] = None
    timestamp: int
    progress_ms: Optional[int] = None
    is_playing: bool
    item: Union[Track, Episode, None] = None
    currently_playing_type: Literal["track", "episode", "ad", "unknown"]
    actions: PlaybackActions


class PlaybackHistory(BaseModel):
    track: Track
    played_at: datetime
    context: PlaybackContext
