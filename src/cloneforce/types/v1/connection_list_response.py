# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConnectionListResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_expired: bool = FieldInfo(alias="isExpired")

    is_valid: bool = FieldInfo(alias="isValid")

    name: str

    setting_type: str = FieldInfo(alias="settingType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    error_reason: Optional[str] = FieldInfo(alias="errorReason", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)


class ConnectionListResponse(BaseModel):
    data: List[Data]
