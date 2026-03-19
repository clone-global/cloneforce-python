# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    is_recurring: Annotated[Literal["true", "false"], PropertyInfo(alias="isRecurring")]
    """Filter by recurring status"""
