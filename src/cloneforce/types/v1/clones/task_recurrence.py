# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TaskRecurrence"]


class TaskRecurrence(BaseModel):
    interval: int

    pattern: Literal["Minutely", "Hourly", "Daily", "Weekly", "Monthly", "Yearly"]

    ends_at: Optional[datetime] = FieldInfo(alias="endsAt", default=None)
