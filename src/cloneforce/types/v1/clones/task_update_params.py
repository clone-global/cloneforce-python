# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .task_recurrence_param import TaskRecurrenceParam

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    clone_id: Required[Annotated[str, PropertyInfo(alias="cloneId")]]

    color: str

    is_recurring: Annotated[bool, PropertyInfo(alias="isRecurring")]

    prompt: str

    recurrence: TaskRecurrenceParam

    starts_at: Annotated[Union[str, datetime], PropertyInfo(alias="startsAt", format="iso8601")]

    title: str
