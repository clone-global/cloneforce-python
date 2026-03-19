# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .clone_headshot import CloneHeadshot

__all__ = ["CloneProfile", "State"]


class State(BaseModel):
    headshot: Literal["none", "generating", "ready", "error"]
    """Generation status: none, generating, ready, error"""

    voice: Literal["none", "generating", "ready", "error"]
    """Generation status: none, generating, ready, error"""


class CloneProfile(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    generation: str

    name: str

    screen_name: str = FieldInfo(alias="screenName")

    status: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    appearance_desc: Optional[str] = FieldInfo(alias="appearanceDesc", default=None)

    birthdate: Optional[datetime] = None

    career_desc: Optional[str] = FieldInfo(alias="careerDesc", default=None)

    childhood_desc: Optional[str] = FieldInfo(alias="childhoodDesc", default=None)

    current_city: Optional[str] = FieldInfo(alias="currentCity", default=None)

    education_desc: Optional[str] = FieldInfo(alias="educationDesc", default=None)

    family_desc: Optional[str] = FieldInfo(alias="familyDesc", default=None)

    finances_desc: Optional[str] = FieldInfo(alias="financesDesc", default=None)

    gender: Optional[str] = None

    headshot: Optional[CloneHeadshot] = None

    hometown: Optional[str] = None

    interests_desc: Optional[str] = FieldInfo(alias="interestsDesc", default=None)

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)

    language: Optional[str] = None

    lifestyle_desc: Optional[str] = FieldInfo(alias="lifestyleDesc", default=None)

    marital_status: Optional[str] = FieldInfo(alias="maritalStatus", default=None)

    nationality: Optional[str] = None

    occupation: Optional[str] = None

    principles_desc: Optional[str] = FieldInfo(alias="principlesDesc", default=None)

    races: Optional[List[str]] = None

    social_circle_desc: Optional[str] = FieldInfo(alias="socialCircleDesc", default=None)

    social_hobbies_desc: Optional[str] = FieldInfo(alias="socialHobbiesDesc", default=None)

    sports_desc: Optional[str] = FieldInfo(alias="sportsDesc", default=None)

    state: Optional[State] = None

    travel_desc: Optional[str] = FieldInfo(alias="travelDesc", default=None)

    unusual_hobbies_desc: Optional[str] = FieldInfo(alias="unusualHobbiesDesc", default=None)

    voice_url: Optional[str] = FieldInfo(alias="voiceUrl", default=None)
