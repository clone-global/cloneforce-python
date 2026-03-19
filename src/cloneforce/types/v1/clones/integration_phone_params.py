# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IntegrationPhoneParams"]


class IntegrationPhoneParams(TypedDict, total=False):
    phone: Required[str]
    """Phone number to purchase (from the available numbers search)"""
