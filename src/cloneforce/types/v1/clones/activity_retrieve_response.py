# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActivityRetrieveResponse", "Skill"]


class Skill(BaseModel):
    is_success: bool = FieldInfo(alias="isSuccess")

    skill_name: str = FieldInfo(alias="skillName")

    result: Optional[str] = None


class ActivityRetrieveResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_success: bool = FieldInfo(alias="isSuccess")

    skill_count: int = FieldInfo(alias="skillCount")

    task_id: str = FieldInfo(alias="taskId")

    response: Optional[str] = None

    skills: Optional[List[Skill]] = None

    task_title: Optional[str] = FieldInfo(alias="taskTitle", default=None)
