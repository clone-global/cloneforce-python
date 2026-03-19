# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["KBFileSummary"]


class KBFileSummary(BaseModel):
    id: str

    content_type: str = FieldInfo(alias="contentType")

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    url: str

    upload_url: Optional[str] = FieldInfo(alias="uploadUrl", default=None)
