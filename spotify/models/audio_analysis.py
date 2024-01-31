from __future__ import annotations

from pydantic import BaseModel


class AudioAnalysisGeneric(BaseModel):
    start: float
    duration: float
    confidence: float


class AudioAnalysisMeta(BaseModel):
    analyzer_version: str
    platform: str
    detailed_status: str
    status_code: int
    timestamp: int
    analysis_time: float
    input_process: str


class AudioAnalysisTrack(BaseModel):
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


class AudioAnalysisSection(BaseModel):
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


class AudioAnalysisSegment(BaseModel):
    start: float
    duration: float
    confidence: float
    loudness_start: float
    loudness_max: float
    loudness_max_time: float
    loudness_end: float
    pitches: list[float]
    timbre: list[float]


class AudioAnalysis(BaseModel):
    meta: AudioAnalysisMeta
    track: AudioAnalysisTrack
    bars: list[AudioAnalysisGeneric]
    beats: list[AudioAnalysisGeneric]
    sections: list[AudioAnalysisSection]
    segments: list[AudioAnalysisSegment]
    tatums: list[AudioAnalysisGeneric]
