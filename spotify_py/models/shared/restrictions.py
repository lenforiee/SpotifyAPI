from __future__ import annotations

from pydantic import BaseModel
from typing import Literal


class Restrictions(BaseModel):
    reason: Literal["market", "product", "explicit", "payment_required"]
