# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OAuthProvision"]


class OAuthProvision(BaseModel):
    connection_id: str = FieldInfo(alias="connectionId")

    provision_url: str = FieldInfo(alias="provisionUrl")
    """URL to present to the user to complete the OAuth consent flow"""
