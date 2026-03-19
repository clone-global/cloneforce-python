# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PhoneListAvailableParams"]


class PhoneListAvailableParams(TypedDict, total=False):
    area_code: Annotated[int, PropertyInfo(alias="areaCode")]
    """Area code filter"""

    country: str
    """Country code (default US)"""

    limit: int
    """Max results (default 20)"""
