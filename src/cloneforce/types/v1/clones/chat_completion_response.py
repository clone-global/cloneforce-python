# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChatCompletionResponse"]


class ChatCompletionResponse(BaseModel):
    id: str

    chat_id: str = FieldInfo(alias="chatId")

    content: str

    created_at: datetime = FieldInfo(alias="createdAt")

    role: str
