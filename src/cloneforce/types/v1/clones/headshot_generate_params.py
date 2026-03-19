# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HeadshotGenerateParams"]


class HeadshotGenerateParams(TypedDict, total=False):
    additional_instructions: Annotated[str, PropertyInfo(alias="additionalInstructions")]
    """Optional instructions to nudge the generation (e.g.

    "deeper voice", "longer hair")
    """
