from __future__ import annotations

from typing import Optional
from typing import Literal

from pydantic import BaseModel
from pydantic import Field


# In documenation this object is camelCase but we pythonify it.
class RecommendationSeed(BaseModel):
    after_filtering_size: int = Field(alias="afterFilteringSize")
    after_relinking_size: int = Field(alias="afterRelinkingSize")
    href: Optional[str] = None
    id: str
    initial_pool_size: int = Field(alias="initialPoolSize")
    type: Literal["artist", "track", "genre"]
