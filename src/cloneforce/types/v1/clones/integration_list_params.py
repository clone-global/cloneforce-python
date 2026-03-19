# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IntegrationListParams"]


class IntegrationListParams(TypedDict, total=False):
    type: Literal["Slack", "Email", "MsTeams", "Phone"]
    """Filter by integration type"""
