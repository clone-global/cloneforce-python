# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SkillUpdateParams", "Setting"]


class SkillUpdateParams(TypedDict, total=False):
    clone_id: Required[Annotated[str, PropertyInfo(alias="cloneId")]]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    settings: Iterable[Setting]


class Setting(TypedDict, total=False):
    name: Required[str]

    connection_id: Annotated[str, PropertyInfo(alias="connectionId")]
    """Required for connection-type settings"""

    value: str
    """Required for non-connection settings"""
