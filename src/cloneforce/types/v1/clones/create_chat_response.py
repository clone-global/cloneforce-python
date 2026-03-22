# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CreateChatResponse"]


class CreateChatResponse(BaseModel):
    id: str

    clone_id: str = FieldInfo(alias="cloneId")

    created_at: datetime = FieldInfo(alias="createdAt")

    title: str
