# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SkillRetrieveResponse", "SettingDefinition", "SettingsConfigured"]


class SettingDefinition(BaseModel):
    is_connection: bool = FieldInfo(alias="isConnection")

    is_required: bool = FieldInfo(alias="isRequired")

    name: str

    description: Optional[str] = None

    setting_type: Optional[str] = FieldInfo(alias="settingType", default=None)


class SettingsConfigured(BaseModel):
    is_configured: bool = FieldInfo(alias="isConfigured")

    is_connection: bool = FieldInfo(alias="isConnection")

    name: str


class SkillRetrieveResponse(BaseModel):
    is_attached: bool = FieldInfo(alias="isAttached")

    logic_type: str = FieldInfo(alias="logicType")

    name: str

    requires_connections: bool = FieldInfo(alias="requiresConnections")

    skill_id: str = FieldInfo(alias="skillId")

    category: Optional[str] = None

    connections_configured: Optional[bool] = FieldInfo(alias="connectionsConfigured", default=None)

    description: Optional[str] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    setting_definitions: Optional[List[SettingDefinition]] = FieldInfo(alias="settingDefinitions", default=None)

    settings_configured: Optional[List[SettingsConfigured]] = FieldInfo(alias="settingsConfigured", default=None)
