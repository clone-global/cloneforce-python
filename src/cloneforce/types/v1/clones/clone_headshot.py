# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CloneHeadshot"]


class CloneHeadshot(BaseModel):
    large: Optional[str] = None

    medium: Optional[str] = None

    small: Optional[str] = None
