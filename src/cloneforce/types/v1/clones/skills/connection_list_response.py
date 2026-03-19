# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .skill_connection_info import SkillConnectionInfo

__all__ = ["ConnectionListResponse"]


class ConnectionListResponse(BaseModel):
    data: List[SkillConnectionInfo]
