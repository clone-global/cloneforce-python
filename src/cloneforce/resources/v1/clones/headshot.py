# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.clones import headshot_generate_params
from ....types.v1.clones.generation_status import GenerationStatus

__all__ = ["HeadshotResource", "AsyncHeadshotResource"]


class HeadshotResource(SyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def with_raw_response(self) -> HeadshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return HeadshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HeadshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return HeadshotResourceWithStreamingResponse(self)

    def generate(
        self,
        clone_id: str,
        *,
        additional_instructions: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationStatus:
        """Triggers asynchronous headshot regeneration for a clone.

        Returns immediately
        with 202 Accepted. Poll `GET /clones/{cloneId}/profile` and check
        `state.headshot` for progress.

        An optional request body can include `additionalInstructions` to nudge the
        appearance (e.g. "longer hair", "wearing glasses"). An empty body performs a
        standard regeneration.

        Args:
          additional_instructions: Optional instructions to nudge the generation (e.g. "deeper voice", "longer
              hair")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._post(
            f"/api/v1/clones/{clone_id}/headshot/generate",
            body=maybe_transform(
                {"additional_instructions": additional_instructions}, headshot_generate_params.HeadshotGenerateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationStatus,
        )


class AsyncHeadshotResource(AsyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def with_raw_response(self) -> AsyncHeadshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHeadshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHeadshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncHeadshotResourceWithStreamingResponse(self)

    async def generate(
        self,
        clone_id: str,
        *,
        additional_instructions: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerationStatus:
        """Triggers asynchronous headshot regeneration for a clone.

        Returns immediately
        with 202 Accepted. Poll `GET /clones/{cloneId}/profile` and check
        `state.headshot` for progress.

        An optional request body can include `additionalInstructions` to nudge the
        appearance (e.g. "longer hair", "wearing glasses"). An empty body performs a
        standard regeneration.

        Args:
          additional_instructions: Optional instructions to nudge the generation (e.g. "deeper voice", "longer
              hair")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._post(
            f"/api/v1/clones/{clone_id}/headshot/generate",
            body=await async_maybe_transform(
                {"additional_instructions": additional_instructions}, headshot_generate_params.HeadshotGenerateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationStatus,
        )


class HeadshotResourceWithRawResponse:
    def __init__(self, headshot: HeadshotResource) -> None:
        self._headshot = headshot

        self.generate = to_raw_response_wrapper(
            headshot.generate,
        )


class AsyncHeadshotResourceWithRawResponse:
    def __init__(self, headshot: AsyncHeadshotResource) -> None:
        self._headshot = headshot

        self.generate = async_to_raw_response_wrapper(
            headshot.generate,
        )


class HeadshotResourceWithStreamingResponse:
    def __init__(self, headshot: HeadshotResource) -> None:
        self._headshot = headshot

        self.generate = to_streamed_response_wrapper(
            headshot.generate,
        )


class AsyncHeadshotResourceWithStreamingResponse:
    def __init__(self, headshot: AsyncHeadshotResource) -> None:
        self._headshot = headshot

        self.generate = async_to_streamed_response_wrapper(
            headshot.generate,
        )
