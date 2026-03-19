# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .integration_summary import IntegrationSummary

__all__ = ["IntegrationListResponse"]


class IntegrationListResponse(BaseModel):
    data: List[IntegrationSummary]
