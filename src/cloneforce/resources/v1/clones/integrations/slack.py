# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.clones.integrations import slack_update_params
from .....types.v1.clones.integrations.slack_integration import SlackIntegration

__all__ = ["SlackResource", "AsyncSlackResource"]


class SlackResource(SyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def with_raw_response(self) -> SlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return SlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return SlackResourceWithStreamingResponse(self)

    def create(
        self,
        clone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackIntegration:
        """
        Creates a pending Slack integration and returns a Slack app manifest for
        installation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._post(
            path_template("/public/v1/clones/{clone_id}/integrations/slack", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackIntegration,
        )

    def update(
        self,
        integration_id: str,
        *,
        clone_id: str,
        bot_token: str | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackIntegration:
        """Configures bot token and signing secret.

        Tests the connection if the bot token
        changes.

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
        return self._patch(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/slack/{integration_id}",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            body=maybe_transform(
                {
                    "bot_token": bot_token,
                    "signing_secret": signing_secret,
                },
                slack_update_params.SlackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackIntegration,
        )


class AsyncSlackResource(AsyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def with_raw_response(self) -> AsyncSlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncSlackResourceWithStreamingResponse(self)

    async def create(
        self,
        clone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackIntegration:
        """
        Creates a pending Slack integration and returns a Slack app manifest for
        installation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._post(
            path_template("/public/v1/clones/{clone_id}/integrations/slack", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackIntegration,
        )

    async def update(
        self,
        integration_id: str,
        *,
        clone_id: str,
        bot_token: str | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SlackIntegration:
        """Configures bot token and signing secret.

        Tests the connection if the bot token
        changes.

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
        return await self._patch(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/slack/{integration_id}",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            body=await async_maybe_transform(
                {
                    "bot_token": bot_token,
                    "signing_secret": signing_secret,
                },
                slack_update_params.SlackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SlackIntegration,
        )


class SlackResourceWithRawResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.create = to_raw_response_wrapper(
            slack.create,
        )
        self.update = to_raw_response_wrapper(
            slack.update,
        )


class AsyncSlackResourceWithRawResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.create = async_to_raw_response_wrapper(
            slack.create,
        )
        self.update = async_to_raw_response_wrapper(
            slack.update,
        )


class SlackResourceWithStreamingResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.create = to_streamed_response_wrapper(
            slack.create,
        )
        self.update = to_streamed_response_wrapper(
            slack.update,
        )


class AsyncSlackResourceWithStreamingResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.create = async_to_streamed_response_wrapper(
            slack.create,
        )
        self.update = async_to_streamed_response_wrapper(
            slack.update,
        )
