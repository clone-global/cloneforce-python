# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OAuthProvision"]


class OAuthProvision(BaseModel):
    connection_id: str = FieldInfo(alias="connectionId")

    provision_url: str = FieldInfo(alias="provisionUrl")
    """Deprecated.

    This URL pointed at the legacy v1 web app's OAuth consent flow, retired in
    September 2026, and no longer resolves. Provision OAuth connections in Studio
    instead. The field is kept so existing clients keep parsing the response.
    """
