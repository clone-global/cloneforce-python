# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ConnectionUpdateParams"]


class ConnectionUpdateParams(TypedDict, total=False):
    clone_id: Required[Annotated[str, PropertyInfo(alias="cloneId")]]

    skill_name: Required[Annotated[str, PropertyInfo(alias="skillName")]]

    connection_id: Required[Annotated[str, PropertyInfo(alias="connectionId")]]
