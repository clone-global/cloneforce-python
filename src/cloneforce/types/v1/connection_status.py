# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConnectionStatus"]


class ConnectionStatus(BaseModel):
    id: str

    is_expired: bool = FieldInfo(alias="isExpired")

    is_valid: bool = FieldInfo(alias="isValid")

    error_reason: Optional[str] = FieldInfo(alias="errorReason", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
