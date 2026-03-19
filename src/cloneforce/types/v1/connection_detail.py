# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConnectionDetail"]


class ConnectionDetail(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_expired: bool = FieldInfo(alias="isExpired")

    is_valid: bool = FieldInfo(alias="isValid")

    name: str

    setting_type: str = FieldInfo(alias="settingType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    acquired_permissions: Optional[List[str]] = FieldInfo(alias="acquiredPermissions", default=None)

    error_reason: Optional[str] = FieldInfo(alias="errorReason", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    extra_fields: Optional[Dict[str, str]] = FieldInfo(alias="extraFields", default=None)
