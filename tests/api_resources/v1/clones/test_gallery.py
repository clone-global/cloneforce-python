# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.clones import (
    GalleryItemSummary,
    GalleryListResponse,
    GalleryDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGallery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cloneforce) -> None:
        gallery = client.v1.clones.gallery.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
        )
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloneforce) -> None:
        gallery = client.v1.clones.gallery.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
            description="description",
            is_hero_video=True,
        )
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cloneforce) -> None:
        response = client.v1.clones.gallery.with_raw_response.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = response.parse()
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cloneforce) -> None:
        with client.v1.clones.gallery.with_streaming_response.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = response.parse()
            assert_matches_type(GalleryItemSummary, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.gallery.with_raw_response.create(
                clone_id="",
                media_url="mediaUrl",
                type="Video",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cloneforce) -> None:
        gallery = client.v1.clones.gallery.retrieve(
            item_id="itemId",
            clone_id="cloneId",
        )
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cloneforce) -> None:
        response = client.v1.clones.gallery.with_raw_response.retrieve(
            item_id="itemId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = response.parse()
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cloneforce) -> None:
        with client.v1.clones.gallery.with_streaming_response.retrieve(
            item_id="itemId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = response.parse()
            assert_matches_type(GalleryItemSummary, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.gallery.with_raw_response.retrieve(
                item_id="itemId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.v1.clones.gallery.with_raw_response.retrieve(
                item_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cloneforce) -> None:
        gallery = client.v1.clones.gallery.list(
            clone_id="cloneId",
        )
        assert_matches_type(GalleryListResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloneforce) -> None:
        gallery = client.v1.clones.gallery.list(
            clone_id="cloneId",
            type="Video",
        )
        assert_matches_type(GalleryListResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cloneforce) -> None:
        response = client.v1.clones.gallery.with_raw_response.list(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = response.parse()
        assert_matches_type(GalleryListResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cloneforce) -> None:
        with client.v1.clones.gallery.with_streaming_response.list(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = response.parse()
            assert_matches_type(GalleryListResponse, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.gallery.with_raw_response.list(
                clone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cloneforce) -> None:
        gallery = client.v1.clones.gallery.delete(
            item_id="itemId",
            clone_id="cloneId",
        )
        assert_matches_type(GalleryDeleteResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cloneforce) -> None:
        response = client.v1.clones.gallery.with_raw_response.delete(
            item_id="itemId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = response.parse()
        assert_matches_type(GalleryDeleteResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cloneforce) -> None:
        with client.v1.clones.gallery.with_streaming_response.delete(
            item_id="itemId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = response.parse()
            assert_matches_type(GalleryDeleteResponse, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.gallery.with_raw_response.delete(
                item_id="itemId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.v1.clones.gallery.with_raw_response.delete(
                item_id="",
                clone_id="cloneId",
            )


class TestAsyncGallery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloneforce) -> None:
        gallery = await async_client.v1.clones.gallery.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
        )
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloneforce) -> None:
        gallery = await async_client.v1.clones.gallery.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
            description="description",
            is_hero_video=True,
        )
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.gallery.with_raw_response.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = await response.parse()
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.gallery.with_streaming_response.create(
            clone_id="cloneId",
            media_url="mediaUrl",
            type="Video",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = await response.parse()
            assert_matches_type(GalleryItemSummary, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.gallery.with_raw_response.create(
                clone_id="",
                media_url="mediaUrl",
                type="Video",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCloneforce) -> None:
        gallery = await async_client.v1.clones.gallery.retrieve(
            item_id="itemId",
            clone_id="cloneId",
        )
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.gallery.with_raw_response.retrieve(
            item_id="itemId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = await response.parse()
        assert_matches_type(GalleryItemSummary, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.gallery.with_streaming_response.retrieve(
            item_id="itemId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = await response.parse()
            assert_matches_type(GalleryItemSummary, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.gallery.with_raw_response.retrieve(
                item_id="itemId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.v1.clones.gallery.with_raw_response.retrieve(
                item_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloneforce) -> None:
        gallery = await async_client.v1.clones.gallery.list(
            clone_id="cloneId",
        )
        assert_matches_type(GalleryListResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloneforce) -> None:
        gallery = await async_client.v1.clones.gallery.list(
            clone_id="cloneId",
            type="Video",
        )
        assert_matches_type(GalleryListResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.gallery.with_raw_response.list(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = await response.parse()
        assert_matches_type(GalleryListResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.gallery.with_streaming_response.list(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = await response.parse()
            assert_matches_type(GalleryListResponse, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.gallery.with_raw_response.list(
                clone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloneforce) -> None:
        gallery = await async_client.v1.clones.gallery.delete(
            item_id="itemId",
            clone_id="cloneId",
        )
        assert_matches_type(GalleryDeleteResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.gallery.with_raw_response.delete(
            item_id="itemId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gallery = await response.parse()
        assert_matches_type(GalleryDeleteResponse, gallery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.gallery.with_streaming_response.delete(
            item_id="itemId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gallery = await response.parse()
            assert_matches_type(GalleryDeleteResponse, gallery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.gallery.with_raw_response.delete(
                item_id="itemId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.v1.clones.gallery.with_raw_response.delete(
                item_id="",
                clone_id="cloneId",
            )
