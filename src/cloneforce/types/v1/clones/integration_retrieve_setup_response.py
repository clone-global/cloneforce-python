# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IntegrationRetrieveSetupResponse"]


class IntegrationRetrieveSetupResponse(BaseModel):
    setup_url: str = FieldInfo(alias="setupUrl")

    type: str
