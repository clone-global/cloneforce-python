# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TaskRecurrenceParam"]


class TaskRecurrenceParam(TypedDict, total=False):
    interval: Required[int]

    pattern: Required[Literal["Minutely", "Hourly", "Daily", "Weekly", "Monthly", "Yearly"]]

    ends_at: Annotated[Union[str, datetime], PropertyInfo(alias="endsAt", format="iso8601")]
