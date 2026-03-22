# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    connection_list_params,
    connection_create_params,
    connection_update_params,
    connection_create_oauth_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.oauth_provision import OAuthProvision
from ...types.v1.connection_detail import ConnectionDetail
from ...types.v1.connection_status import ConnectionStatus
from ...types.v1.connection_list_response import ConnectionListResponse
from ...types.v1.connection_delete_response import ConnectionDeleteResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    """Organization-level connection credential management"""

    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return ConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        key: str,
        name: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDetail:
        """
        Creates a new key-value connection credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/public/v1/connections",
            body=maybe_transform(
                {
                    "key": key,
                    "name": name,
                    "value": value,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDetail,
        )

    def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDetail:
        """
        Get a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/public/v1/connections/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDetail,
        )

    def update(
        self,
        connection_id: str,
        *,
        key: str | Omit = omit,
        name: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDetail:
        """Updates name, key, and/or value on a standard connection.

        OAuth connections
        cannot be updated here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._patch(
            path_template("/public/v1/connections/{connection_id}", connection_id=connection_id),
            body=maybe_transform(
                {
                    "key": key,
                    "name": name,
                    "value": value,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDetail,
        )

    def list(
        self,
        *,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """
        Returns all connections in the organization.

        Args:
          type: Filter by setting type (e.g. Standard, or an OAuth provider type)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, connection_list_params.ConnectionListParams),
            ),
            cast_to=ConnectionListResponse,
        )

    def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDeleteResponse:
        """
        Delete a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._delete(
            path_template("/public/v1/connections/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDeleteResponse,
        )

    def create_oauth(
        self,
        *,
        name: str,
        setting_type: str,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthProvision:
        """Creates a pending OAuth connection and returns a provision URL.

        Present the
        provision URL to the user to complete the OAuth consent flow.

        Args:
          setting_type: Must be an OAuth provider type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/public/v1/connections/oauth",
            body=maybe_transform(
                {
                    "name": name,
                    "setting_type": setting_type,
                    "scopes": scopes,
                },
                connection_create_oauth_params.ConnectionCreateOAuthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthProvision,
        )

    def get_status(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionStatus:
        """
        Returns lightweight validity and expiration status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template("/public/v1/connections/{connection_id}/status", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionStatus,
        )

    def refresh(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionStatus:
        """Refreshes OAuth tokens for a connection.

        Only supported for refreshable
        connection types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            path_template("/public/v1/connections/{connection_id}/refresh", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionStatus,
        )

    def reprovision_oauth(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthProvision:
        """
        Returns a new provision URL for an existing OAuth connection to re-authorize.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            path_template("/public/v1/connections/{connection_id}/reprovision", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthProvision,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    """Organization-level connection credential management"""

    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        key: str,
        name: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDetail:
        """
        Creates a new key-value connection credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/public/v1/connections",
            body=await async_maybe_transform(
                {
                    "key": key,
                    "name": name,
                    "value": value,
                },
                connection_create_params.ConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDetail,
        )

    async def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDetail:
        """
        Get a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/public/v1/connections/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDetail,
        )

    async def update(
        self,
        connection_id: str,
        *,
        key: str | Omit = omit,
        name: str | Omit = omit,
        value: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDetail:
        """Updates name, key, and/or value on a standard connection.

        OAuth connections
        cannot be updated here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._patch(
            path_template("/public/v1/connections/{connection_id}", connection_id=connection_id),
            body=await async_maybe_transform(
                {
                    "key": key,
                    "name": name,
                    "value": value,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDetail,
        )

    async def list(
        self,
        *,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """
        Returns all connections in the organization.

        Args:
          type: Filter by setting type (e.g. Standard, or an OAuth provider type)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/v1/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, connection_list_params.ConnectionListParams),
            ),
            cast_to=ConnectionListResponse,
        )

    async def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionDeleteResponse:
        """
        Delete a connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._delete(
            path_template("/public/v1/connections/{connection_id}", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionDeleteResponse,
        )

    async def create_oauth(
        self,
        *,
        name: str,
        setting_type: str,
        scopes: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthProvision:
        """Creates a pending OAuth connection and returns a provision URL.

        Present the
        provision URL to the user to complete the OAuth consent flow.

        Args:
          setting_type: Must be an OAuth provider type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/public/v1/connections/oauth",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "setting_type": setting_type,
                    "scopes": scopes,
                },
                connection_create_oauth_params.ConnectionCreateOAuthParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthProvision,
        )

    async def get_status(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionStatus:
        """
        Returns lightweight validity and expiration status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template("/public/v1/connections/{connection_id}/status", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionStatus,
        )

    async def refresh(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionStatus:
        """Refreshes OAuth tokens for a connection.

        Only supported for refreshable
        connection types.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            path_template("/public/v1/connections/{connection_id}/refresh", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionStatus,
        )

    async def reprovision_oauth(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthProvision:
        """
        Returns a new provision URL for an existing OAuth connection to re-authorize.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            path_template("/public/v1/connections/{connection_id}/reprovision", connection_id=connection_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthProvision,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connections.update,
        )
        self.list = to_raw_response_wrapper(
            connections.list,
        )
        self.delete = to_raw_response_wrapper(
            connections.delete,
        )
        self.create_oauth = to_raw_response_wrapper(
            connections.create_oauth,
        )
        self.get_status = to_raw_response_wrapper(
            connections.get_status,
        )
        self.refresh = to_raw_response_wrapper(
            connections.refresh,
        )
        self.reprovision_oauth = to_raw_response_wrapper(
            connections.reprovision_oauth,
        )


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_raw_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connections.delete,
        )
        self.create_oauth = async_to_raw_response_wrapper(
            connections.create_oauth,
        )
        self.get_status = async_to_raw_response_wrapper(
            connections.get_status,
        )
        self.refresh = async_to_raw_response_wrapper(
            connections.refresh,
        )
        self.reprovision_oauth = async_to_raw_response_wrapper(
            connections.reprovision_oauth,
        )


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.create = to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connections.update,
        )
        self.list = to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            connections.delete,
        )
        self.create_oauth = to_streamed_response_wrapper(
            connections.create_oauth,
        )
        self.get_status = to_streamed_response_wrapper(
            connections.get_status,
        )
        self.refresh = to_streamed_response_wrapper(
            connections.refresh,
        )
        self.reprovision_oauth = to_streamed_response_wrapper(
            connections.reprovision_oauth,
        )


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.create = async_to_streamed_response_wrapper(
            connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connections.delete,
        )
        self.create_oauth = async_to_streamed_response_wrapper(
            connections.create_oauth,
        )
        self.get_status = async_to_streamed_response_wrapper(
            connections.get_status,
        )
        self.refresh = async_to_streamed_response_wrapper(
            connections.refresh,
        )
        self.reprovision_oauth = async_to_streamed_response_wrapper(
            connections.reprovision_oauth,
        )
