# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
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
from .....types.v1.clones.skills import connection_update_params
from .....types.v1.clones.skills.skill_connection_info import SkillConnectionInfo
from .....types.v1.clones.skills.connection_list_response import ConnectionListResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    """Skill marketplace search and clone skill management"""

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

    def update(
        self,
        setting_name: str,
        *,
        clone_id: str,
        skill_name: str,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillConnectionInfo:
        """
        Assigns a connection to a connection-type setting on a clone skill.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not skill_name:
            raise ValueError(f"Expected a non-empty value for `skill_name` but received {skill_name!r}")
        if not setting_name:
            raise ValueError(f"Expected a non-empty value for `setting_name` but received {setting_name!r}")
        return self._put(
            path_template(
                "/api/v1/clones/{clone_id}/skills/{skill_name}/connections/{setting_name}",
                clone_id=clone_id,
                skill_name=skill_name,
                setting_name=setting_name,
            ),
            body=maybe_transform({"connection_id": connection_id}, connection_update_params.ConnectionUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillConnectionInfo,
        )

    def list(
        self,
        skill_name: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """
        Returns connection-type settings for a skill on a clone, with their
        configuration status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not skill_name:
            raise ValueError(f"Expected a non-empty value for `skill_name` but received {skill_name!r}")
        return self._get(
            path_template(
                "/api/v1/clones/{clone_id}/skills/{skill_name}/connections", clone_id=clone_id, skill_name=skill_name
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionListResponse,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    """Skill marketplace search and clone skill management"""

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

    async def update(
        self,
        setting_name: str,
        *,
        clone_id: str,
        skill_name: str,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillConnectionInfo:
        """
        Assigns a connection to a connection-type setting on a clone skill.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not skill_name:
            raise ValueError(f"Expected a non-empty value for `skill_name` but received {skill_name!r}")
        if not setting_name:
            raise ValueError(f"Expected a non-empty value for `setting_name` but received {setting_name!r}")
        return await self._put(
            path_template(
                "/api/v1/clones/{clone_id}/skills/{skill_name}/connections/{setting_name}",
                clone_id=clone_id,
                skill_name=skill_name,
                setting_name=setting_name,
            ),
            body=await async_maybe_transform(
                {"connection_id": connection_id}, connection_update_params.ConnectionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillConnectionInfo,
        )

    async def list(
        self,
        skill_name: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionListResponse:
        """
        Returns connection-type settings for a skill on a clone, with their
        configuration status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not skill_name:
            raise ValueError(f"Expected a non-empty value for `skill_name` but received {skill_name!r}")
        return await self._get(
            path_template(
                "/api/v1/clones/{clone_id}/skills/{skill_name}/connections", clone_id=clone_id, skill_name=skill_name
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionListResponse,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.update = to_raw_response_wrapper(
            connections.update,
        )
        self.list = to_raw_response_wrapper(
            connections.list,
        )


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.update = async_to_raw_response_wrapper(
            connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            connections.list,
        )


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.update = to_streamed_response_wrapper(
            connections.update,
        )
        self.list = to_streamed_response_wrapper(
            connections.list,
        )


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.update = async_to_streamed_response_wrapper(
            connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
