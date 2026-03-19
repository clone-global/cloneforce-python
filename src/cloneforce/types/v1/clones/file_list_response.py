# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .kb_file_summary import KBFileSummary

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
    data: List[KBFileSummary]
