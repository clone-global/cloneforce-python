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
from ....types.v1.integrations import phone_list_available_params
from ....types.v1.integrations.phone_list_available_response import PhoneListAvailableResponse

__all__ = ["PhoneResource", "AsyncPhoneResource"]


class PhoneResource(SyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def with_raw_response(self) -> PhoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return PhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#with_streaming_response
        """
        return PhoneResourceWithStreamingResponse(self)

    def list_available(
        self,
        *,
        area_code: int | Omit = omit,
        country: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneListAvailableResponse:
        """
        Searches for available phone numbers via Twilio that can be purchased.

        Args:
          area_code: Area code filter

          country: Country code (default US)

          limit: Max results (default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/integrations/phone/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "area_code": area_code,
                        "country": country,
                        "limit": limit,
                    },
                    phone_list_available_params.PhoneListAvailableParams,
                ),
            ),
            cast_to=PhoneListAvailableResponse,
        )


class AsyncPhoneResource(AsyncAPIResource):
    """Clone integration management (Slack, Email, MS Teams, Phone)"""

    @cached_property
    def with_raw_response(self) -> AsyncPhoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#with_streaming_response
        """
        return AsyncPhoneResourceWithStreamingResponse(self)

    async def list_available(
        self,
        *,
        area_code: int | Omit = omit,
        country: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneListAvailableResponse:
        """
        Searches for available phone numbers via Twilio that can be purchased.

        Args:
          area_code: Area code filter

          country: Country code (default US)

          limit: Max results (default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/integrations/phone/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "area_code": area_code,
                        "country": country,
                        "limit": limit,
                    },
                    phone_list_available_params.PhoneListAvailableParams,
                ),
            ),
            cast_to=PhoneListAvailableResponse,
        )


class PhoneResourceWithRawResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.list_available = to_raw_response_wrapper(
            phone.list_available,
        )


class AsyncPhoneResourceWithRawResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.list_available = async_to_raw_response_wrapper(
            phone.list_available,
        )


class PhoneResourceWithStreamingResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.list_available = to_streamed_response_wrapper(
            phone.list_available,
        )


class AsyncPhoneResourceWithStreamingResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.list_available = async_to_streamed_response_wrapper(
            phone.list_available,
        )
