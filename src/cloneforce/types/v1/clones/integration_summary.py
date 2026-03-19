# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .integrations.ms_teams_team_ref import MsTeamsTeamRef

__all__ = [
    "IntegrationSummary",
    "Detail",
    "DetailSlackDetail",
    "DetailEmailDetail",
    "DetailMsTeamsDetail",
    "DetailPhoneDetail",
]


class DetailSlackDetail(BaseModel):
    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    team_name: Optional[str] = FieldInfo(alias="teamName", default=None)


class DetailEmailDetail(BaseModel):
    email: str

    connection_type: Optional[str] = FieldInfo(alias="connectionType", default=None)


class DetailMsTeamsDetail(BaseModel):
    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)

    teams: Optional[List[MsTeamsTeamRef]] = None


class DetailPhoneDetail(BaseModel):
    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)


Detail: TypeAlias = Union[DetailSlackDetail, DetailEmailDetail, DetailMsTeamsDetail, DetailPhoneDetail]


class IntegrationSummary(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    status: Literal["Pending", "Connected", "Error", "Provisioning"]

    type: Literal["Slack", "Email", "MsTeams", "Phone"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    detail: Optional[Detail] = None
    """Type-specific integration details"""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    name: Optional[str] = None
