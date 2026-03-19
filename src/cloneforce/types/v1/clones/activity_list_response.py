# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActivityListResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_success: bool = FieldInfo(alias="isSuccess")

    task_id: str = FieldInfo(alias="taskId")

    response: Optional[str] = None

    task_title: Optional[str] = FieldInfo(alias="taskTitle", default=None)


class ActivityListResponse(BaseModel):
    data: List[Data]
