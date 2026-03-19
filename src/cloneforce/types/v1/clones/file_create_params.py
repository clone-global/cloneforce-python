# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    url: Required[str]

    content_type: Annotated[str, PropertyInfo(alias="contentType")]

    name: str
