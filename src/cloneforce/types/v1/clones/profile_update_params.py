# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    appearance_desc: Annotated[str, PropertyInfo(alias="appearanceDesc")]

    birthdate: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    career_desc: Annotated[str, PropertyInfo(alias="careerDesc")]

    childhood_desc: Annotated[str, PropertyInfo(alias="childhoodDesc")]

    current_city: Annotated[str, PropertyInfo(alias="currentCity")]

    education_desc: Annotated[str, PropertyInfo(alias="educationDesc")]

    family_desc: Annotated[str, PropertyInfo(alias="familyDesc")]

    finances_desc: Annotated[str, PropertyInfo(alias="financesDesc")]

    gender: str

    hometown: str

    interests_desc: Annotated[str, PropertyInfo(alias="interestsDesc")]

    is_enabled: Annotated[bool, PropertyInfo(alias="isEnabled")]

    language: str

    lifestyle_desc: Annotated[str, PropertyInfo(alias="lifestyleDesc")]

    marital_status: Annotated[str, PropertyInfo(alias="maritalStatus")]

    name: str

    nationality: str

    occupation: str

    principles_desc: Annotated[str, PropertyInfo(alias="principlesDesc")]

    races: SequenceNotStr[str]

    screen_name: Annotated[str, PropertyInfo(alias="screenName")]

    social_circle_desc: Annotated[str, PropertyInfo(alias="socialCircleDesc")]

    social_hobbies_desc: Annotated[str, PropertyInfo(alias="socialHobbiesDesc")]

    sports_desc: Annotated[str, PropertyInfo(alias="sportsDesc")]

    travel_desc: Annotated[str, PropertyInfo(alias="travelDesc")]

    unusual_hobbies_desc: Annotated[str, PropertyInfo(alias="unusualHobbiesDesc")]
