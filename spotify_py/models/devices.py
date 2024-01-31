from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class Device(BaseModel):
    id: Optional[str] = None
    is_active: bool
    is_private_session: bool
    is_restricted: bool
    name: str
    type: str  # TODO: add literal types here
    volume_percent: Optional[int] = None
    supports_volume: bool
