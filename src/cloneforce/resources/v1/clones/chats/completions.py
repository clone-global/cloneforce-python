# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._streaming import Stream, AsyncStream
from ....._base_client import make_request_options
from .....types.v1.clones.chats import completion_create_params
from .....types.v1.clones.chat_completion_response import ChatCompletionResponse
from .....types.v1.clones.chats.chat_completion_chunk import ChatCompletionChunk

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    """Chat sessions and completions"""

    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletionResponse:
        """
        Sends a user message to the clone and returns the assistant's response.

        Set `stream: true` to receive the response as Server-Sent Events (SSE). SSE
        events: `message.delta` (incremental text), `message.completed` (final message),
        `done` (stream end).

        Args:
          message: The user message to send to the clone

          stream: If true, response is streamed as SSE events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ChatCompletionChunk]:
        """
        Sends a user message to the clone and returns the assistant's response.

        Set `stream: true` to receive the response as Server-Sent Events (SSE). SSE
        events: `message.delta` (incremental text), `message.completed` (final message),
        `done` (stream end).

        Args:
          message: The user message to send to the clone

          stream: If true, response is streamed as SSE events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletionResponse | Stream[ChatCompletionChunk]:
        """
        Sends a user message to the clone and returns the assistant's response.

        Set `stream: true` to receive the response as Server-Sent Events (SSE). SSE
        events: `message.delta` (incremental text), `message.completed` (final message),
        `done` (stream end).

        Args:
          message: The user message to send to the clone

          stream: If true, response is streamed as SSE events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["clone_id", "message"], ["clone_id", "message", "stream"])
    def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletionResponse | Stream[ChatCompletionChunk]:
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template(
                "/public/v1/clones/{clone_id}/chats/{chat_id}/completions", clone_id=clone_id, chat_id=chat_id
            ),
            body=maybe_transform(
                {
                    "message": message,
                    "stream": stream,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionResponse,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )


class AsyncCompletionsResource(AsyncAPIResource):
    """Chat sessions and completions"""

    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletionResponse:
        """
        Sends a user message to the clone and returns the assistant's response.

        Set `stream: true` to receive the response as Server-Sent Events (SSE). SSE
        events: `message.delta` (incremental text), `message.completed` (final message),
        `done` (stream end).

        Args:
          message: The user message to send to the clone

          stream: If true, response is streamed as SSE events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ChatCompletionChunk]:
        """
        Sends a user message to the clone and returns the assistant's response.

        Set `stream: true` to receive the response as Server-Sent Events (SSE). SSE
        events: `message.delta` (incremental text), `message.completed` (final message),
        `done` (stream end).

        Args:
          message: The user message to send to the clone

          stream: If true, response is streamed as SSE events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletionResponse | AsyncStream[ChatCompletionChunk]:
        """
        Sends a user message to the clone and returns the assistant's response.

        Set `stream: true` to receive the response as Server-Sent Events (SSE). SSE
        events: `message.delta` (incremental text), `message.completed` (final message),
        `done` (stream end).

        Args:
          message: The user message to send to the clone

          stream: If true, response is streamed as SSE events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["clone_id", "message"], ["clone_id", "message", "stream"])
    async def create(
        self,
        chat_id: str,
        *,
        clone_id: str,
        message: str,
        stream: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletionResponse | AsyncStream[ChatCompletionChunk]:
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template(
                "/public/v1/clones/{clone_id}/chats/{chat_id}/completions", clone_id=clone_id, chat_id=chat_id
            ),
            body=await async_maybe_transform(
                {
                    "message": message,
                    "stream": stream,
                },
                completion_create_params.CompletionCreateParamsStreaming
                if stream
                else completion_create_params.CompletionCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletionResponse,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
