# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SkillSearchParams"]


class SkillSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    clone_id: Annotated[str, PropertyInfo(alias="cloneId")]
    """Clone ID to check attachment status against"""
