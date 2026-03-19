# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .phone import (
    PhoneResource,
    AsyncPhoneResource,
    PhoneResourceWithRawResponse,
    AsyncPhoneResourceWithRawResponse,
    PhoneResourceWithStreamingResponse,
    AsyncPhoneResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def phone(self) -> PhoneResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return PhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def phone(self) -> AsyncPhoneResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncPhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def phone(self) -> PhoneResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return PhoneResourceWithRawResponse(self._integrations.phone)


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncPhoneResourceWithRawResponse(self._integrations.phone)


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def phone(self) -> PhoneResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return PhoneResourceWithStreamingResponse(self._integrations.phone)


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncPhoneResourceWithStreamingResponse(self._integrations.phone)
