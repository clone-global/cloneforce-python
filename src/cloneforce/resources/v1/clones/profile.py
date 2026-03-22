# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.v1.clones import profile_update_params
from ....types.v1.clones.clone_profile import CloneProfile

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        clone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneProfile:
        """
        Returns the full profile and aesthetics for a clone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._get(
            path_template("/public/v1/clones/{clone_id}/profile", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneProfile,
        )

    def update(
        self,
        clone_id: str,
        *,
        appearance_desc: str | Omit = omit,
        birthdate: Union[str, datetime] | Omit = omit,
        career_desc: str | Omit = omit,
        childhood_desc: str | Omit = omit,
        current_city: str | Omit = omit,
        education_desc: str | Omit = omit,
        family_desc: str | Omit = omit,
        finances_desc: str | Omit = omit,
        gender: str | Omit = omit,
        hometown: str | Omit = omit,
        interests_desc: str | Omit = omit,
        is_enabled: bool | Omit = omit,
        language: str | Omit = omit,
        lifestyle_desc: str | Omit = omit,
        marital_status: str | Omit = omit,
        name: str | Omit = omit,
        nationality: str | Omit = omit,
        occupation: str | Omit = omit,
        principles_desc: str | Omit = omit,
        races: SequenceNotStr[str] | Omit = omit,
        screen_name: str | Omit = omit,
        social_circle_desc: str | Omit = omit,
        social_hobbies_desc: str | Omit = omit,
        sports_desc: str | Omit = omit,
        travel_desc: str | Omit = omit,
        unusual_hobbies_desc: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneProfile:
        """Updates one or more fields on a clone's profile.

        Only provided fields are
        changed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._patch(
            path_template("/public/v1/clones/{clone_id}/profile", clone_id=clone_id),
            body=maybe_transform(
                {
                    "appearance_desc": appearance_desc,
                    "birthdate": birthdate,
                    "career_desc": career_desc,
                    "childhood_desc": childhood_desc,
                    "current_city": current_city,
                    "education_desc": education_desc,
                    "family_desc": family_desc,
                    "finances_desc": finances_desc,
                    "gender": gender,
                    "hometown": hometown,
                    "interests_desc": interests_desc,
                    "is_enabled": is_enabled,
                    "language": language,
                    "lifestyle_desc": lifestyle_desc,
                    "marital_status": marital_status,
                    "name": name,
                    "nationality": nationality,
                    "occupation": occupation,
                    "principles_desc": principles_desc,
                    "races": races,
                    "screen_name": screen_name,
                    "social_circle_desc": social_circle_desc,
                    "social_hobbies_desc": social_hobbies_desc,
                    "sports_desc": sports_desc,
                    "travel_desc": travel_desc,
                    "unusual_hobbies_desc": unusual_hobbies_desc,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneProfile,
        )


class AsyncProfileResource(AsyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        clone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneProfile:
        """
        Returns the full profile and aesthetics for a clone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._get(
            path_template("/public/v1/clones/{clone_id}/profile", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneProfile,
        )

    async def update(
        self,
        clone_id: str,
        *,
        appearance_desc: str | Omit = omit,
        birthdate: Union[str, datetime] | Omit = omit,
        career_desc: str | Omit = omit,
        childhood_desc: str | Omit = omit,
        current_city: str | Omit = omit,
        education_desc: str | Omit = omit,
        family_desc: str | Omit = omit,
        finances_desc: str | Omit = omit,
        gender: str | Omit = omit,
        hometown: str | Omit = omit,
        interests_desc: str | Omit = omit,
        is_enabled: bool | Omit = omit,
        language: str | Omit = omit,
        lifestyle_desc: str | Omit = omit,
        marital_status: str | Omit = omit,
        name: str | Omit = omit,
        nationality: str | Omit = omit,
        occupation: str | Omit = omit,
        principles_desc: str | Omit = omit,
        races: SequenceNotStr[str] | Omit = omit,
        screen_name: str | Omit = omit,
        social_circle_desc: str | Omit = omit,
        social_hobbies_desc: str | Omit = omit,
        sports_desc: str | Omit = omit,
        travel_desc: str | Omit = omit,
        unusual_hobbies_desc: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneProfile:
        """Updates one or more fields on a clone's profile.

        Only provided fields are
        changed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._patch(
            path_template("/public/v1/clones/{clone_id}/profile", clone_id=clone_id),
            body=await async_maybe_transform(
                {
                    "appearance_desc": appearance_desc,
                    "birthdate": birthdate,
                    "career_desc": career_desc,
                    "childhood_desc": childhood_desc,
                    "current_city": current_city,
                    "education_desc": education_desc,
                    "family_desc": family_desc,
                    "finances_desc": finances_desc,
                    "gender": gender,
                    "hometown": hometown,
                    "interests_desc": interests_desc,
                    "is_enabled": is_enabled,
                    "language": language,
                    "lifestyle_desc": lifestyle_desc,
                    "marital_status": marital_status,
                    "name": name,
                    "nationality": nationality,
                    "occupation": occupation,
                    "principles_desc": principles_desc,
                    "races": races,
                    "screen_name": screen_name,
                    "social_circle_desc": social_circle_desc,
                    "social_hobbies_desc": social_hobbies_desc,
                    "sports_desc": sports_desc,
                    "travel_desc": travel_desc,
                    "unusual_hobbies_desc": unusual_hobbies_desc,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneProfile,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = to_raw_response_wrapper(
            profile.update,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            profile.update,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            profile.update,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            profile.update,
        )
