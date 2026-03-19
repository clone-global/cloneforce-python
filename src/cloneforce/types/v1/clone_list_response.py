# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .clones.clone_headshot import CloneHeadshot

__all__ = ["CloneListResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    generation: str

    name: str

    screen_name: str = FieldInfo(alias="screenName")

    status: str

    headshot: Optional[CloneHeadshot] = None

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)


class CloneListResponse(BaseModel):
    data: List[Data]
