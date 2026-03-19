# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SkillSummary"]


class SkillSummary(BaseModel):
    accuracy: float

    is_active: bool = FieldInfo(alias="isActive")

    is_system_skill: bool = FieldInfo(alias="isSystemSkill")

    name: str

    total_runs: int = FieldInfo(alias="totalRuns")

    category: Optional[str] = None

    description: Optional[str] = None

    skill_id: Optional[str] = FieldInfo(alias="skillId", default=None)
