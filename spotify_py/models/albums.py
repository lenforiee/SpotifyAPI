from __future__ import annotations

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from spotify_py.models.base import GenericList
from spotify_py.models.base import ExternalUrls
from spotify_py.models.base import Image
from spotify_py.models.base import Copyright
from spotify_py.models.base import Restrictions
from spotify_py.models.base import ExternalIds

from spotify_py.models.artists import SimplifiedArtist


class TrackRecommendationSeed(BaseModel):
    after_filtering_size: int
    after_relinking_size: int
    href: str
    id: str
    initial_pool_size: int
    type: str


class TrackAudioAnalysisMeta(BaseModel):
    analyzer_version: str
    platform: str
    detailed_status: str
    status_code: int
    timestamp: int
    analysis_time: float
    input_process: str


class TrackAudioAnalysisTrack(BaseModel):
    num_samples: int
    duration: float
    sample_md5: str
    offset_seconds: int
    window_seconds: int
    analysis_sample_rate: int
    analysis_channels: int
    end_of_fade_in: float
    start_of_fade_out: float
    loudness: float
    tempo: float
    tempo_confidence: float
    time_signature: int
    time_signature_confidence: float
    key: int
    key_confidence: float
    mode: int
    mode_confidence: float
    codestring: str
    code_version: float
    echoprintstring: str
    echoprint_version: float
    synchstring: str
    synch_version: float
    rhythmstring: str
    rhythm_version: float


class TrackAudioAnalysisBar(BaseModel):
    start: float
    duration: float
    confidence: float


class TrackAudioAnalysisBeat(BaseModel):
    start: float
    duration: float
    confidence: float


class TrackAudioAnalysisSection(BaseModel):
    start: float
    duration: float
    confidence: float
    loudness: float
    tempo: float
    tempo_confidence: float
    key: int
    key_confidence: float
    mode: int
    mode_confidence: float
    time_signature: int
    time_signature_confidence: float


class TrackAudioAnalysisSegment(BaseModel):
    start: float
    duration: float
    confidence: float
    loudness_start: float
    loudness_max: float
    loudness_max_time: float
    loudness_end: float
    pitches: list[float]
    timbre: list[float]


class TrackAudioAnalysisTatum(BaseModel):
    start: float
    duration: float
    confidence: float


class TrackAudioAnalysis(BaseModel):
    meta: TrackAudioAnalysisMeta
    track: TrackAudioAnalysisTrack
    bars: list[TrackAudioAnalysisBar]
    beats: list[TrackAudioAnalysisBeat]
    sections: list[TrackAudioAnalysisSection]
    segments: list[TrackAudioAnalysisSegment]
    tatums: list[TrackAudioAnalysisTatum]


class TrackAudioFeatures(BaseModel):
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: int
    energy: float
    id: str
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    speechiness: float
    tempo: float
    time_signature: int
    track_href: str
    type: str
    uri: str
    valence: float


class RelinkedTrack(BaseModel):
    external_urls: ExternalUrls
    href: str
    id: str
    type: str
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
    linked_from: Optional[RelinkedTrack] = None
    restrictions: Optional[Restrictions] = None
    name: str
    preview_url: Optional[str] = None
    track_number: int
    type: str
    uri: str
    is_local: bool


class Track(SimplifiedTrack):
    album: SimplifiedAlbum
    external_ids: ExternalIds
    popularity: int


class SimplifiedAlbum(BaseModel):
    album_type: str
    total_tracks: int
    available_markets: list[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    name: str
    release_date: str
    release_date_precision: str
    restrictions: Optional[Restrictions] = None
    type: str
    uri: str
    artists: list[SimplifiedArtist]


# Get Album
# Get Several Albums
class Album(SimplifiedAlbum):
    tracks: GenericList[SimplifiedTrack]
    copyrights: list[Copyright]
    external_ids: ExternalIds
    genres: list[str]
    label: str
    popularity: int


class SavedAlbum(BaseModel):
    added_at: datetime
    album: Album


# Get Album Tracks (SimplifiedTrack)
# Get user saved albums (SavedAlbum)
# Get new releases (SimplifiedAlbum)
