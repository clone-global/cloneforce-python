# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["GalleryItemSummary"]


class GalleryItemSummary(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    type: Literal["Video", "Audio", "Image"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str

    description: Optional[str] = None

    is_hero_video: Optional[bool] = FieldInfo(alias="isHeroVideo", default=None)

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)
