# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ConnectionCreateOAuthParams"]


class ConnectionCreateOAuthParams(TypedDict, total=False):
    name: Required[str]

    setting_type: Required[Annotated[str, PropertyInfo(alias="settingType")]]
    """Must be an OAuth provider type"""

    scopes: SequenceNotStr[str]
