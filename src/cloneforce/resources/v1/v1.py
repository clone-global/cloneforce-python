# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .skills import (
    SkillsResource,
    AsyncSkillsResource,
    SkillsResourceWithRawResponse,
    AsyncSkillsResourceWithRawResponse,
    SkillsResourceWithStreamingResponse,
    AsyncSkillsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .connections import (
    ConnectionsResource,
    AsyncConnectionsResource,
    ConnectionsResourceWithRawResponse,
    AsyncConnectionsResourceWithRawResponse,
    ConnectionsResourceWithStreamingResponse,
    AsyncConnectionsResourceWithStreamingResponse,
)
from .clones.clones import (
    ClonesResource,
    AsyncClonesResource,
    ClonesResourceWithRawResponse,
    AsyncClonesResourceWithRawResponse,
    ClonesResourceWithStreamingResponse,
    AsyncClonesResourceWithStreamingResponse,
)
from .integrations.integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def clones(self) -> ClonesResource:
        """Clone profile management and asset generation"""
        return ClonesResource(self._client)

    @cached_property
    def skills(self) -> SkillsResource:
        """Skill marketplace search and clone skill management"""
        return SkillsResource(self._client)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def connections(self) -> ConnectionsResource:
        """Organization-level connection credential management"""
        return ConnectionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def clones(self) -> AsyncClonesResource:
        """Clone profile management and asset generation"""
        return AsyncClonesResource(self._client)

    @cached_property
    def skills(self) -> AsyncSkillsResource:
        """Skill marketplace search and clone skill management"""
        return AsyncSkillsResource(self._client)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def connections(self) -> AsyncConnectionsResource:
        """Organization-level connection credential management"""
        return AsyncConnectionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clones(self) -> ClonesResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return ClonesResourceWithRawResponse(self._v1.clones)

    @cached_property
    def skills(self) -> SkillsResourceWithRawResponse:
        """Skill marketplace search and clone skill management"""
        return SkillsResourceWithRawResponse(self._v1.skills)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._v1.integrations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithRawResponse:
        """Organization-level connection credential management"""
        return ConnectionsResourceWithRawResponse(self._v1.connections)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clones(self) -> AsyncClonesResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return AsyncClonesResourceWithRawResponse(self._v1.clones)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithRawResponse:
        """Skill marketplace search and clone skill management"""
        return AsyncSkillsResourceWithRawResponse(self._v1.skills)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._v1.integrations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithRawResponse:
        """Organization-level connection credential management"""
        return AsyncConnectionsResourceWithRawResponse(self._v1.connections)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clones(self) -> ClonesResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return ClonesResourceWithStreamingResponse(self._v1.clones)

    @cached_property
    def skills(self) -> SkillsResourceWithStreamingResponse:
        """Skill marketplace search and clone skill management"""
        return SkillsResourceWithStreamingResponse(self._v1.skills)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._v1.integrations)

    @cached_property
    def connections(self) -> ConnectionsResourceWithStreamingResponse:
        """Organization-level connection credential management"""
        return ConnectionsResourceWithStreamingResponse(self._v1.connections)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def clones(self) -> AsyncClonesResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return AsyncClonesResourceWithStreamingResponse(self._v1.clones)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithStreamingResponse:
        """Skill marketplace search and clone skill management"""
        return AsyncSkillsResourceWithStreamingResponse(self._v1.skills)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._v1.integrations)

    @cached_property
    def connections(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """Organization-level connection credential management"""
        return AsyncConnectionsResourceWithStreamingResponse(self._v1.connections)
