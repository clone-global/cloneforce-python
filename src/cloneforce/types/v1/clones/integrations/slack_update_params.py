# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SlackUpdateParams"]


class SlackUpdateParams(TypedDict, total=False):
    clone_id: Required[Annotated[str, PropertyInfo(alias="cloneId")]]

    bot_token: Annotated[str, PropertyInfo(alias="botToken")]

    signing_secret: Annotated[str, PropertyInfo(alias="signingSecret")]
