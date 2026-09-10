# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IntegrationGetSetupURLResponse"]


class IntegrationGetSetupURLResponse(BaseModel):
    setup_url: str = FieldInfo(alias="setupUrl")
    """Deprecated.

    This URL pointed at the legacy v1 web app, retired in September 2026, and no
    longer resolves to a setup page. Complete the integration setup in Studio
    instead. The field is kept so existing clients keep parsing the response.
    """

    type: str
