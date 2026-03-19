# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IntegrationPhoneResponse"]


class IntegrationPhoneResponse(BaseModel):
    id: str

    phone_number: str = FieldInfo(alias="phoneNumber")

    status: str
