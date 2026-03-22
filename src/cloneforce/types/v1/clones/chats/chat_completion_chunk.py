# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["ChatCompletionChunk", "Delta"]


class Delta(BaseModel):
    content: Optional[str] = None


class ChatCompletionChunk(BaseModel):
    """SSE message.delta event payload"""

    id: str

    delta: Optional[Delta] = None
