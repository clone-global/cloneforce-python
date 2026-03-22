# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .slack import (
    SlackResource,
    AsyncSlackResource,
    SlackResourceWithRawResponse,
    AsyncSlackResourceWithRawResponse,
    SlackResourceWithStreamingResponse,
    AsyncSlackResourceWithStreamingResponse,
)
from .msteams import (
    MsteamsResource,
    AsyncMsteamsResource,
    MsteamsResourceWithRawResponse,
    AsyncMsteamsResourceWithRawResponse,
    MsteamsResourceWithStreamingResponse,
    AsyncMsteamsResourceWithStreamingResponse,
)
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
from .....types.v1.clones import integration_list_params, integration_create_phone_params
from .....types.v1.clones.integration_summary import IntegrationSummary
from .....types.v1.clones.integration_list_response import IntegrationListResponse
from .....types.v1.clones.integration_delete_response import IntegrationDeleteResponse
from .....types.v1.clones.integration_create_phone_response import IntegrationCreatePhoneResponse
from .....types.v1.clones.integration_get_setup_url_response import IntegrationGetSetupURLResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def slack(self) -> SlackResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return SlackResource(self._client)

    @cached_property
    def msteams(self) -> MsteamsResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return MsteamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        integration_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationSummary:
        """
        Get an integration

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
        return self._get(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/{integration_id}",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSummary,
        )

    def list(
        self,
        clone_id: str,
        *,
        type: Literal["Slack", "Email", "MsTeams", "Phone"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListResponse:
        """
        Returns all integrations for a clone (Slack, Email, MS Teams, Phone).

        Args:
          type: Filter by integration type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._get(
            path_template("/public/v1/clones/{clone_id}/integrations", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, integration_list_params.IntegrationListParams),
            ),
            cast_to=IntegrationListResponse,
        )

    def delete(
        self,
        integration_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationDeleteResponse:
        """Deletes an integration and performs type-specific cleanup (e.g.

        Twilio release
        for phone).

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
        return self._delete(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/{integration_id}",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationDeleteResponse,
        )

    def create_phone(
        self,
        clone_id: str,
        *,
        phone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreatePhoneResponse:
        """Purchases a phone number and provisions it for clone voice calls.

        Requires
        sufficient account credits. Creates a Twilio number, ElevenLabs voice agent, and
        billing subscription.

        Args:
          phone: Phone number to purchase (from the available numbers search)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._post(
            path_template("/public/v1/clones/{clone_id}/integrations/phone", clone_id=clone_id),
            body=maybe_transform({"phone": phone}, integration_create_phone_params.IntegrationCreatePhoneParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreatePhoneResponse,
        )

    def get_setup_url(
        self,
        integration_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationGetSetupURLResponse:
        """Returns a browser URL for the OAuth-based setup flow.

        Supported types: `email`,
        `msteams`. Present this URL to the user and poll the integrations list to detect
        completion.

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
        return self._get(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/{integration_id}/setup",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationGetSetupURLResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def slack(self) -> AsyncSlackResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncSlackResource(self._client)

    @cached_property
    def msteams(self) -> AsyncMsteamsResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncMsteamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        integration_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationSummary:
        """
        Get an integration

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
        return await self._get(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/{integration_id}",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSummary,
        )

    async def list(
        self,
        clone_id: str,
        *,
        type: Literal["Slack", "Email", "MsTeams", "Phone"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationListResponse:
        """
        Returns all integrations for a clone (Slack, Email, MS Teams, Phone).

        Args:
          type: Filter by integration type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._get(
            path_template("/public/v1/clones/{clone_id}/integrations", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, integration_list_params.IntegrationListParams),
            ),
            cast_to=IntegrationListResponse,
        )

    async def delete(
        self,
        integration_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationDeleteResponse:
        """Deletes an integration and performs type-specific cleanup (e.g.

        Twilio release
        for phone).

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
        return await self._delete(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/{integration_id}",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationDeleteResponse,
        )

    async def create_phone(
        self,
        clone_id: str,
        *,
        phone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreatePhoneResponse:
        """Purchases a phone number and provisions it for clone voice calls.

        Requires
        sufficient account credits. Creates a Twilio number, ElevenLabs voice agent, and
        billing subscription.

        Args:
          phone: Phone number to purchase (from the available numbers search)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._post(
            path_template("/public/v1/clones/{clone_id}/integrations/phone", clone_id=clone_id),
            body=await async_maybe_transform(
                {"phone": phone}, integration_create_phone_params.IntegrationCreatePhoneParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreatePhoneResponse,
        )

    async def get_setup_url(
        self,
        integration_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationGetSetupURLResponse:
        """Returns a browser URL for the OAuth-based setup flow.

        Supported types: `email`,
        `msteams`. Present this URL to the user and poll the integrations list to detect
        completion.

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
        return await self._get(
            path_template(
                "/public/v1/clones/{clone_id}/integrations/{integration_id}/setup",
                clone_id=clone_id,
                integration_id=integration_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationGetSetupURLResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = to_raw_response_wrapper(
            integrations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            integrations.list,
        )
        self.delete = to_raw_response_wrapper(
            integrations.delete,
        )
        self.create_phone = to_raw_response_wrapper(
            integrations.create_phone,
        )
        self.get_setup_url = to_raw_response_wrapper(
            integrations.get_setup_url,
        )

    @cached_property
    def slack(self) -> SlackResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return SlackResourceWithRawResponse(self._integrations.slack)

    @cached_property
    def msteams(self) -> MsteamsResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return MsteamsResourceWithRawResponse(self._integrations.msteams)


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = async_to_raw_response_wrapper(
            integrations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            integrations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            integrations.delete,
        )
        self.create_phone = async_to_raw_response_wrapper(
            integrations.create_phone,
        )
        self.get_setup_url = async_to_raw_response_wrapper(
            integrations.get_setup_url,
        )

    @cached_property
    def slack(self) -> AsyncSlackResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncSlackResourceWithRawResponse(self._integrations.slack)

    @cached_property
    def msteams(self) -> AsyncMsteamsResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncMsteamsResourceWithRawResponse(self._integrations.msteams)


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = to_streamed_response_wrapper(
            integrations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            integrations.list,
        )
        self.delete = to_streamed_response_wrapper(
            integrations.delete,
        )
        self.create_phone = to_streamed_response_wrapper(
            integrations.create_phone,
        )
        self.get_setup_url = to_streamed_response_wrapper(
            integrations.get_setup_url,
        )

    @cached_property
    def slack(self) -> SlackResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return SlackResourceWithStreamingResponse(self._integrations.slack)

    @cached_property
    def msteams(self) -> MsteamsResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return MsteamsResourceWithStreamingResponse(self._integrations.msteams)


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = async_to_streamed_response_wrapper(
            integrations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            integrations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            integrations.delete,
        )
        self.create_phone = async_to_streamed_response_wrapper(
            integrations.create_phone,
        )
        self.get_setup_url = async_to_streamed_response_wrapper(
            integrations.get_setup_url,
        )

    @cached_property
    def slack(self) -> AsyncSlackResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncSlackResourceWithStreamingResponse(self._integrations.slack)

    @cached_property
    def msteams(self) -> AsyncMsteamsResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncMsteamsResourceWithStreamingResponse(self._integrations.msteams)
