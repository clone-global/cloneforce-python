# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PhoneListAvailableResponse", "Data"]


class Data(BaseModel):
    friendly_name: str = FieldInfo(alias="friendlyName")

    phone: str

    country: Optional[str] = None

    locality: Optional[str] = None

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    region: Optional[str] = None


class PhoneListAvailableResponse(BaseModel):
    data: List[Data]
