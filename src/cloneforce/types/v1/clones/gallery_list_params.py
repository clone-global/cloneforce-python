# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GalleryListParams"]


class GalleryListParams(TypedDict, total=False):
    type: Literal["Video", "Audio", "Image"]
    """Filter by media type"""
