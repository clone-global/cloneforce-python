# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .task_summary import TaskSummary

__all__ = ["TaskListResponse"]


class TaskListResponse(BaseModel):
    data: List[TaskSummary]
