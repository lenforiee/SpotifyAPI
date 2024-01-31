from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class Restrictions(BaseModel):
    reason: Literal["market", "product", "explicit", "payment_required"]
