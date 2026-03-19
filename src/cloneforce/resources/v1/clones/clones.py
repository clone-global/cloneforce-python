# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .voice import (
    VoiceResource,
    AsyncVoiceResource,
    VoiceResourceWithRawResponse,
    AsyncVoiceResourceWithRawResponse,
    VoiceResourceWithStreamingResponse,
    AsyncVoiceResourceWithStreamingResponse,
)
from .gallery import (
    GalleryResource,
    AsyncGalleryResource,
    GalleryResourceWithRawResponse,
    AsyncGalleryResourceWithRawResponse,
    GalleryResourceWithStreamingResponse,
    AsyncGalleryResourceWithStreamingResponse,
)
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from .activity import (
    ActivityResource,
    AsyncActivityResource,
    ActivityResourceWithRawResponse,
    AsyncActivityResourceWithRawResponse,
    ActivityResourceWithStreamingResponse,
    AsyncActivityResourceWithStreamingResponse,
)
from .headshot import (
    HeadshotResource,
    AsyncHeadshotResource,
    HeadshotResourceWithRawResponse,
    AsyncHeadshotResourceWithRawResponse,
    HeadshotResourceWithStreamingResponse,
    AsyncHeadshotResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .skills.skills import (
    SkillsResource,
    AsyncSkillsResource,
    SkillsResourceWithRawResponse,
    AsyncSkillsResourceWithRawResponse,
    SkillsResourceWithStreamingResponse,
    AsyncSkillsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .integrations.integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
)
from ....types.v1.clone_list_response import CloneListResponse

__all__ = ["ClonesResource", "AsyncClonesResource"]


class ClonesResource(SyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def profile(self) -> ProfileResource:
        """Clone profile management and asset generation"""
        return ProfileResource(self._client)

    @cached_property
    def voice(self) -> VoiceResource:
        """Clone profile management and asset generation"""
        return VoiceResource(self._client)

    @cached_property
    def headshot(self) -> HeadshotResource:
        """Clone profile management and asset generation"""
        return HeadshotResource(self._client)

    @cached_property
    def skills(self) -> SkillsResource:
        """Skill marketplace search and clone skill management"""
        return SkillsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        """Scheduled task management"""
        return TasksResource(self._client)

    @cached_property
    def files(self) -> FilesResource:
        """Clone knowledge base file management"""
        return FilesResource(self._client)

    @cached_property
    def gallery(self) -> GalleryResource:
        """Clone gallery media management"""
        return GalleryResource(self._client)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return IntegrationsResource(self._client)

    @cached_property
    def activity(self) -> ActivityResource:
        """Task run history"""
        return ActivityResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return ClonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#with_streaming_response
        """
        return ClonesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneListResponse:
        """Returns all clones in the organization, ordered by creation date descending."""
        return self._get(
            "/api/v1/clones",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneListResponse,
        )


class AsyncClonesResource(AsyncAPIResource):
    """Clone profile management and asset generation"""

    @cached_property
    def profile(self) -> AsyncProfileResource:
        """Clone profile management and asset generation"""
        return AsyncProfileResource(self._client)

    @cached_property
    def voice(self) -> AsyncVoiceResource:
        """Clone profile management and asset generation"""
        return AsyncVoiceResource(self._client)

    @cached_property
    def headshot(self) -> AsyncHeadshotResource:
        """Clone profile management and asset generation"""
        return AsyncHeadshotResource(self._client)

    @cached_property
    def skills(self) -> AsyncSkillsResource:
        """Skill marketplace search and clone skill management"""
        return AsyncSkillsResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        """Scheduled task management"""
        return AsyncTasksResource(self._client)

    @cached_property
    def files(self) -> AsyncFilesResource:
        """Clone knowledge base file management"""
        return AsyncFilesResource(self._client)

    @cached_property
    def gallery(self) -> AsyncGalleryResource:
        """Clone gallery media management"""
        return AsyncGalleryResource(self._client)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def activity(self) -> AsyncActivityResource:
        """Task run history"""
        return AsyncActivityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cloneforce-python#with_streaming_response
        """
        return AsyncClonesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloneListResponse:
        """Returns all clones in the organization, ordered by creation date descending."""
        return await self._get(
            "/api/v1/clones",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloneListResponse,
        )


class ClonesResourceWithRawResponse:
    def __init__(self, clones: ClonesResource) -> None:
        self._clones = clones

        self.list = to_raw_response_wrapper(
            clones.list,
        )

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return ProfileResourceWithRawResponse(self._clones.profile)

    @cached_property
    def voice(self) -> VoiceResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return VoiceResourceWithRawResponse(self._clones.voice)

    @cached_property
    def headshot(self) -> HeadshotResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return HeadshotResourceWithRawResponse(self._clones.headshot)

    @cached_property
    def skills(self) -> SkillsResourceWithRawResponse:
        """Skill marketplace search and clone skill management"""
        return SkillsResourceWithRawResponse(self._clones.skills)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        """Scheduled task management"""
        return TasksResourceWithRawResponse(self._clones.tasks)

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        """Clone knowledge base file management"""
        return FilesResourceWithRawResponse(self._clones.files)

    @cached_property
    def gallery(self) -> GalleryResourceWithRawResponse:
        """Clone gallery media management"""
        return GalleryResourceWithRawResponse(self._clones.gallery)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return IntegrationsResourceWithRawResponse(self._clones.integrations)

    @cached_property
    def activity(self) -> ActivityResourceWithRawResponse:
        """Task run history"""
        return ActivityResourceWithRawResponse(self._clones.activity)


class AsyncClonesResourceWithRawResponse:
    def __init__(self, clones: AsyncClonesResource) -> None:
        self._clones = clones

        self.list = async_to_raw_response_wrapper(
            clones.list,
        )

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return AsyncProfileResourceWithRawResponse(self._clones.profile)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return AsyncVoiceResourceWithRawResponse(self._clones.voice)

    @cached_property
    def headshot(self) -> AsyncHeadshotResourceWithRawResponse:
        """Clone profile management and asset generation"""
        return AsyncHeadshotResourceWithRawResponse(self._clones.headshot)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithRawResponse:
        """Skill marketplace search and clone skill management"""
        return AsyncSkillsResourceWithRawResponse(self._clones.skills)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        """Scheduled task management"""
        return AsyncTasksResourceWithRawResponse(self._clones.tasks)

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        """Clone knowledge base file management"""
        return AsyncFilesResourceWithRawResponse(self._clones.files)

    @cached_property
    def gallery(self) -> AsyncGalleryResourceWithRawResponse:
        """Clone gallery media management"""
        return AsyncGalleryResourceWithRawResponse(self._clones.gallery)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncIntegrationsResourceWithRawResponse(self._clones.integrations)

    @cached_property
    def activity(self) -> AsyncActivityResourceWithRawResponse:
        """Task run history"""
        return AsyncActivityResourceWithRawResponse(self._clones.activity)


class ClonesResourceWithStreamingResponse:
    def __init__(self, clones: ClonesResource) -> None:
        self._clones = clones

        self.list = to_streamed_response_wrapper(
            clones.list,
        )

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return ProfileResourceWithStreamingResponse(self._clones.profile)

    @cached_property
    def voice(self) -> VoiceResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return VoiceResourceWithStreamingResponse(self._clones.voice)

    @cached_property
    def headshot(self) -> HeadshotResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return HeadshotResourceWithStreamingResponse(self._clones.headshot)

    @cached_property
    def skills(self) -> SkillsResourceWithStreamingResponse:
        """Skill marketplace search and clone skill management"""
        return SkillsResourceWithStreamingResponse(self._clones.skills)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        """Scheduled task management"""
        return TasksResourceWithStreamingResponse(self._clones.tasks)

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        """Clone knowledge base file management"""
        return FilesResourceWithStreamingResponse(self._clones.files)

    @cached_property
    def gallery(self) -> GalleryResourceWithStreamingResponse:
        """Clone gallery media management"""
        return GalleryResourceWithStreamingResponse(self._clones.gallery)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return IntegrationsResourceWithStreamingResponse(self._clones.integrations)

    @cached_property
    def activity(self) -> ActivityResourceWithStreamingResponse:
        """Task run history"""
        return ActivityResourceWithStreamingResponse(self._clones.activity)


class AsyncClonesResourceWithStreamingResponse:
    def __init__(self, clones: AsyncClonesResource) -> None:
        self._clones = clones

        self.list = async_to_streamed_response_wrapper(
            clones.list,
        )

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return AsyncProfileResourceWithStreamingResponse(self._clones.profile)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return AsyncVoiceResourceWithStreamingResponse(self._clones.voice)

    @cached_property
    def headshot(self) -> AsyncHeadshotResourceWithStreamingResponse:
        """Clone profile management and asset generation"""
        return AsyncHeadshotResourceWithStreamingResponse(self._clones.headshot)

    @cached_property
    def skills(self) -> AsyncSkillsResourceWithStreamingResponse:
        """Skill marketplace search and clone skill management"""
        return AsyncSkillsResourceWithStreamingResponse(self._clones.skills)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        """Scheduled task management"""
        return AsyncTasksResourceWithStreamingResponse(self._clones.tasks)

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        """Clone knowledge base file management"""
        return AsyncFilesResourceWithStreamingResponse(self._clones.files)

    @cached_property
    def gallery(self) -> AsyncGalleryResourceWithStreamingResponse:
        """Clone gallery media management"""
        return AsyncGalleryResourceWithStreamingResponse(self._clones.gallery)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """Clone integration management (Slack, Email, MS Teams, Phone)"""
        return AsyncIntegrationsResourceWithStreamingResponse(self._clones.integrations)

    @cached_property
    def activity(self) -> AsyncActivityResourceWithStreamingResponse:
        """Task run history"""
        return AsyncActivityResourceWithStreamingResponse(self._clones.activity)
