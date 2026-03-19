# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GalleryCreateParams"]


class GalleryCreateParams(TypedDict, total=False):
    media_url: Required[Annotated[str, PropertyInfo(alias="mediaUrl")]]
    """URL of the media file to download and add to the gallery"""

    type: Required[Literal["Video", "Audio", "Image"]]

    description: str

    is_hero_video: Annotated[bool, PropertyInfo(alias="isHeroVideo")]
