# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SkillCreateParams"]


class SkillCreateParams(TypedDict, total=False):
    skill_id: Required[Annotated[str, PropertyInfo(alias="skillId")]]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
