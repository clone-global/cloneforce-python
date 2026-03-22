# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import skill_search_params, skill_retrieve_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.skill_search_response import SkillSearchResponse
from ...types.v1.skill_retrieve_response import SkillRetrieveResponse

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    """Skill marketplace search and clone skill management"""

    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return SkillsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        skill_id: str,
        *,
        clone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillRetrieveResponse:
        """Returns full skill details including setting definitions.

        If `cloneId` is
        provided, also returns attachment and configuration status.

        Args:
          clone_id: Clone ID to check attachment and configuration status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return self._get(
            path_template("/public/v1/skills/{skill_id}", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"clone_id": clone_id}, skill_retrieve_params.SkillRetrieveParams),
            ),
            cast_to=SkillRetrieveResponse,
        )

    def search(
        self,
        *,
        q: str,
        clone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillSearchResponse:
        """Searches the skill marketplace.

        Optionally marks results already attached to a
        clone.

        Args:
          q: Search query

          clone_id: Clone ID to check attachment status against

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public/v1/skills/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "clone_id": clone_id,
                    },
                    skill_search_params.SkillSearchParams,
                ),
            ),
            cast_to=SkillSearchResponse,
        )


class AsyncSkillsResource(AsyncAPIResource):
    """Skill marketplace search and clone skill management"""

    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        skill_id: str,
        *,
        clone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillRetrieveResponse:
        """Returns full skill details including setting definitions.

        If `cloneId` is
        provided, also returns attachment and configuration status.

        Args:
          clone_id: Clone ID to check attachment and configuration status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not skill_id:
            raise ValueError(f"Expected a non-empty value for `skill_id` but received {skill_id!r}")
        return await self._get(
            path_template("/public/v1/skills/{skill_id}", skill_id=skill_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"clone_id": clone_id}, skill_retrieve_params.SkillRetrieveParams),
            ),
            cast_to=SkillRetrieveResponse,
        )

    async def search(
        self,
        *,
        q: str,
        clone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SkillSearchResponse:
        """Searches the skill marketplace.

        Optionally marks results already attached to a
        clone.

        Args:
          q: Search query

          clone_id: Clone ID to check attachment status against

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public/v1/skills/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "clone_id": clone_id,
                    },
                    skill_search_params.SkillSearchParams,
                ),
            ),
            cast_to=SkillSearchResponse,
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.retrieve = to_raw_response_wrapper(
            skills.retrieve,
        )
        self.search = to_raw_response_wrapper(
            skills.search,
        )


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.retrieve = async_to_raw_response_wrapper(
            skills.retrieve,
        )
        self.search = async_to_raw_response_wrapper(
            skills.search,
        )


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.retrieve = to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.search = to_streamed_response_wrapper(
            skills.search,
        )


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.retrieve = async_to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.search = async_to_streamed_response_wrapper(
            skills.search,
        )
