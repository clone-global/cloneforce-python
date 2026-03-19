# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .task_recurrence import TaskRecurrence

__all__ = ["TaskSummary"]


class TaskSummary(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_recurring: bool = FieldInfo(alias="isRecurring")

    prompt: str

    starts_at: datetime = FieldInfo(alias="startsAt")

    title: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    color: Optional[str] = None

    last_ran_at: Optional[datetime] = FieldInfo(alias="lastRanAt", default=None)

    recurrence: Optional[TaskRecurrence] = None
