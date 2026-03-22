# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.clones import voice_generate_params
from ....types.v1.clones.generation_status import GenerationStatus

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)

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
        """Triggers asynchronous voice regeneration for a clone.

        Returns immediately with
        202 Accepted. Poll `GET /clones/{cloneId}/profile` and check `state.voice` for
        progress.

        An optional request body can include `additionalInstructions` to nudge the voice
        style (e.g. "deeper voice", "more energetic"). An empty body performs a standard
        regeneration.

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
            path_template("/public/v1/clones/{clone_id}/voice/generate", clone_id=clone_id),
            body=maybe_transform(
                {"additional_instructions": additional_instructions}, voice_generate_params.VoiceGenerateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationStatus,
        )


class AsyncVoiceResource(AsyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)

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
        """Triggers asynchronous voice regeneration for a clone.

        Returns immediately with
        202 Accepted. Poll `GET /clones/{cloneId}/profile` and check `state.voice` for
        progress.

        An optional request body can include `additionalInstructions` to nudge the voice
        style (e.g. "deeper voice", "more energetic"). An empty body performs a standard
        regeneration.

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
            path_template("/public/v1/clones/{clone_id}/voice/generate", clone_id=clone_id),
            body=await async_maybe_transform(
                {"additional_instructions": additional_instructions}, voice_generate_params.VoiceGenerateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerationStatus,
        )


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.generate = to_raw_response_wrapper(
            voice.generate,
        )


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.generate = async_to_raw_response_wrapper(
            voice.generate,
        )


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.generate = to_streamed_response_wrapper(
            voice.generate,
        )


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.generate = async_to_streamed_response_wrapper(
            voice.generate,
        )
