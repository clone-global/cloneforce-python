# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from .ms_teams_team_ref import MsTeamsTeamRef

__all__ = ["MsteamTeamsResponse"]


class MsteamTeamsResponse(BaseModel):
    id: str

    status: str

    organization_name: Optional[str] = FieldInfo(alias="organizationName", default=None)

    teams: Optional[List[MsTeamsTeamRef]] = None
