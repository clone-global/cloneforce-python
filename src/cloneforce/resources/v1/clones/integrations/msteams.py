# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.clones.integrations import msteam_teams_params
from .....types.v1.clones.integrations.msteam_teams_response import MsteamTeamsResponse

__all__ = ["MsteamsResource", "AsyncMsteamsResource"]


class MsteamsResource(SyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def with_raw_response(self) -> MsteamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return MsteamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MsteamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return MsteamsResourceWithStreamingResponse(self)

    def teams(
        self,
        integration_id: str,
        *,
        clone_id: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MsteamTeamsResponse:
        """Adds a team to an existing MS Teams integration.

        Validates team access via MS
        Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            f"/api/v1/clones/{clone_id}/integrations/msteams/{integration_id}/teams",
            body=maybe_transform({"team_id": team_id}, msteam_teams_params.MsteamTeamsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MsteamTeamsResponse,
        )


class AsyncMsteamsResource(AsyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def with_raw_response(self) -> AsyncMsteamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMsteamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMsteamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncMsteamsResourceWithStreamingResponse(self)

    async def teams(
        self,
        integration_id: str,
        *,
        clone_id: str,
        team_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MsteamTeamsResponse:
        """Adds a team to an existing MS Teams integration.

        Validates team access via MS
        Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            f"/api/v1/clones/{clone_id}/integrations/msteams/{integration_id}/teams",
            body=await async_maybe_transform({"team_id": team_id}, msteam_teams_params.MsteamTeamsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MsteamTeamsResponse,
        )


class MsteamsResourceWithRawResponse:
    def __init__(self, msteams: MsteamsResource) -> None:
        self._msteams = msteams

        self.teams = to_raw_response_wrapper(
            msteams.teams,
        )


class AsyncMsteamsResourceWithRawResponse:
    def __init__(self, msteams: AsyncMsteamsResource) -> None:
        self._msteams = msteams

        self.teams = async_to_raw_response_wrapper(
            msteams.teams,
        )


class MsteamsResourceWithStreamingResponse:
    def __init__(self, msteams: MsteamsResource) -> None:
        self._msteams = msteams

        self.teams = to_streamed_response_wrapper(
            msteams.teams,
        )


class AsyncMsteamsResourceWithStreamingResponse:
    def __init__(self, msteams: AsyncMsteamsResource) -> None:
        self._msteams = msteams

        self.teams = async_to_streamed_response_wrapper(
            msteams.teams,
        )
