# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["SkillConnectionInfo"]


class SkillConnectionInfo(BaseModel):
    is_configured: bool = FieldInfo(alias="isConfigured")

    setting_name: str = FieldInfo(alias="settingName")

    setting_type: str = FieldInfo(alias="settingType")

    connection_id: Optional[str] = FieldInfo(alias="connectionId", default=None)

    is_valid: Optional[bool] = FieldInfo(alias="isValid", default=None)
