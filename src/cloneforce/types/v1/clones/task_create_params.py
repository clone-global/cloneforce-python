# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .task_recurrence_param import TaskRecurrenceParam

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    prompt: Required[str]

    starts_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startsAt", format="iso8601")]]

    title: Required[str]

    color: str

    is_recurring: Annotated[bool, PropertyInfo(alias="isRecurring")]

    recurrence: TaskRecurrenceParam
