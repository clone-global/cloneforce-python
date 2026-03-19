# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SkillSearchResponse", "Data"]


class Data(BaseModel):
    is_already_attached: bool = FieldInfo(alias="isAlreadyAttached")

    name: str

    skill_id: str = FieldInfo(alias="skillId")

    description: Optional[str] = None

    score: Optional[float] = None


class SkillSearchResponse(BaseModel):
    data: List[Data]
