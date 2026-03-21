# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.v1.clones import gallery_list_params, gallery_create_params
from ....types.v1.clones.gallery_item_summary import GalleryItemSummary
from ....types.v1.clones.gallery_list_response import GalleryListResponse
from ....types.v1.clones.gallery_delete_response import GalleryDeleteResponse

__all__ = ["GalleryResource", "AsyncGalleryResource"]


class GalleryResource(SyncAPIResource):
    """Clone gallery media management"""

    @cached_property
    def with_raw_response(self) -> GalleryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return GalleryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GalleryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return GalleryResourceWithStreamingResponse(self)

    def create(
        self,
        clone_id: str,
        *,
        media_url: str,
        type: Literal["Video", "Audio", "Image"],
        description: str | Omit = omit,
        is_hero_video: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryItemSummary:
        """
        Downloads media from the provided URL and adds it to the clone's gallery.

        Args:
          media_url: URL of the media file to download and add to the gallery

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._post(
            path_template("/api/v1/clones/{clone_id}/gallery", clone_id=clone_id),
            body=maybe_transform(
                {
                    "media_url": media_url,
                    "type": type,
                    "description": description,
                    "is_hero_video": is_hero_video,
                },
                gallery_create_params.GalleryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GalleryItemSummary,
        )

    def retrieve(
        self,
        item_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryItemSummary:
        """
        Get a gallery item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template("/api/v1/clones/{clone_id}/gallery/{item_id}", clone_id=clone_id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GalleryItemSummary,
        )

    def list(
        self,
        clone_id: str,
        *,
        type: Literal["Video", "Audio", "Image"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryListResponse:
        """
        List gallery items

        Args:
          type: Filter by media type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return self._get(
            path_template("/api/v1/clones/{clone_id}/gallery", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, gallery_list_params.GalleryListParams),
            ),
            cast_to=GalleryListResponse,
        )

    def delete(
        self,
        item_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryDeleteResponse:
        """
        Delete a gallery item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._delete(
            path_template("/api/v1/clones/{clone_id}/gallery/{item_id}", clone_id=clone_id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GalleryDeleteResponse,
        )


class AsyncGalleryResource(AsyncAPIResource):
    """Clone gallery media management"""

    @cached_property
    def with_raw_response(self) -> AsyncGalleryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clone-global/cloneforce-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGalleryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGalleryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clone-global/cloneforce-python#with_streaming_response
        """
        return AsyncGalleryResourceWithStreamingResponse(self)

    async def create(
        self,
        clone_id: str,
        *,
        media_url: str,
        type: Literal["Video", "Audio", "Image"],
        description: str | Omit = omit,
        is_hero_video: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryItemSummary:
        """
        Downloads media from the provided URL and adds it to the clone's gallery.

        Args:
          media_url: URL of the media file to download and add to the gallery

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._post(
            path_template("/api/v1/clones/{clone_id}/gallery", clone_id=clone_id),
            body=await async_maybe_transform(
                {
                    "media_url": media_url,
                    "type": type,
                    "description": description,
                    "is_hero_video": is_hero_video,
                },
                gallery_create_params.GalleryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GalleryItemSummary,
        )

    async def retrieve(
        self,
        item_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryItemSummary:
        """
        Get a gallery item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template("/api/v1/clones/{clone_id}/gallery/{item_id}", clone_id=clone_id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GalleryItemSummary,
        )

    async def list(
        self,
        clone_id: str,
        *,
        type: Literal["Video", "Audio", "Image"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryListResponse:
        """
        List gallery items

        Args:
          type: Filter by media type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        return await self._get(
            path_template("/api/v1/clones/{clone_id}/gallery", clone_id=clone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, gallery_list_params.GalleryListParams),
            ),
            cast_to=GalleryListResponse,
        )

    async def delete(
        self,
        item_id: str,
        *,
        clone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GalleryDeleteResponse:
        """
        Delete a gallery item

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not clone_id:
            raise ValueError(f"Expected a non-empty value for `clone_id` but received {clone_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._delete(
            path_template("/api/v1/clones/{clone_id}/gallery/{item_id}", clone_id=clone_id, item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GalleryDeleteResponse,
        )


class GalleryResourceWithRawResponse:
    def __init__(self, gallery: GalleryResource) -> None:
        self._gallery = gallery

        self.create = to_raw_response_wrapper(
            gallery.create,
        )
        self.retrieve = to_raw_response_wrapper(
            gallery.retrieve,
        )
        self.list = to_raw_response_wrapper(
            gallery.list,
        )
        self.delete = to_raw_response_wrapper(
            gallery.delete,
        )


class AsyncGalleryResourceWithRawResponse:
    def __init__(self, gallery: AsyncGalleryResource) -> None:
        self._gallery = gallery

        self.create = async_to_raw_response_wrapper(
            gallery.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            gallery.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            gallery.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gallery.delete,
        )


class GalleryResourceWithStreamingResponse:
    def __init__(self, gallery: GalleryResource) -> None:
        self._gallery = gallery

        self.create = to_streamed_response_wrapper(
            gallery.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            gallery.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            gallery.list,
        )
        self.delete = to_streamed_response_wrapper(
            gallery.delete,
        )


class AsyncGalleryResourceWithStreamingResponse:
    def __init__(self, gallery: AsyncGalleryResource) -> None:
        self._gallery = gallery

        self.create = async_to_streamed_response_wrapper(
            gallery.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            gallery.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            gallery.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gallery.delete,
        )
