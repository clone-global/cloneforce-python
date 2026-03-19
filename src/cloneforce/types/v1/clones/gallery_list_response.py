# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .gallery_item_summary import GalleryItemSummary

__all__ = ["GalleryListResponse"]


class GalleryListResponse(BaseModel):
    data: List[GalleryItemSummary]
