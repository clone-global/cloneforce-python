# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["SlackIntegration"]


class SlackIntegration(BaseModel):
    id: str

    status: str

    manifest: Optional[str] = None

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    team_name: Optional[str] = FieldInfo(alias="teamName", default=None)
