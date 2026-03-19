# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.clones import ActivityListResponse, ActivityDeleteResponse, ActivityRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActivity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cloneforce) -> None:
        activity = client.v1.clones.activity.retrieve(
            activity_id="activityId",
            clone_id="cloneId",
        )
        assert_matches_type(ActivityRetrieveResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cloneforce) -> None:
        response = client.v1.clones.activity.with_raw_response.retrieve(
            activity_id="activityId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ActivityRetrieveResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cloneforce) -> None:
        with client.v1.clones.activity.with_streaming_response.retrieve(
            activity_id="activityId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ActivityRetrieveResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.activity.with_raw_response.retrieve(
                activity_id="activityId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `activity_id` but received ''"):
            client.v1.clones.activity.with_raw_response.retrieve(
                activity_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cloneforce) -> None:
        activity = client.v1.clones.activity.list(
            "cloneId",
        )
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cloneforce) -> None:
        response = client.v1.clones.activity.with_raw_response.list(
            "cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cloneforce) -> None:
        with client.v1.clones.activity.with_streaming_response.list(
            "cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ActivityListResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.activity.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cloneforce) -> None:
        activity = client.v1.clones.activity.delete(
            activity_id="activityId",
            clone_id="cloneId",
        )
        assert_matches_type(ActivityDeleteResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cloneforce) -> None:
        response = client.v1.clones.activity.with_raw_response.delete(
            activity_id="activityId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(ActivityDeleteResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cloneforce) -> None:
        with client.v1.clones.activity.with_streaming_response.delete(
            activity_id="activityId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(ActivityDeleteResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.activity.with_raw_response.delete(
                activity_id="activityId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `activity_id` but received ''"):
            client.v1.clones.activity.with_raw_response.delete(
                activity_id="",
                clone_id="cloneId",
            )


class TestAsyncActivity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCloneforce) -> None:
        activity = await async_client.v1.clones.activity.retrieve(
            activity_id="activityId",
            clone_id="cloneId",
        )
        assert_matches_type(ActivityRetrieveResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.activity.with_raw_response.retrieve(
            activity_id="activityId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ActivityRetrieveResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.activity.with_streaming_response.retrieve(
            activity_id="activityId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ActivityRetrieveResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.activity.with_raw_response.retrieve(
                activity_id="activityId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `activity_id` but received ''"):
            await async_client.v1.clones.activity.with_raw_response.retrieve(
                activity_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloneforce) -> None:
        activity = await async_client.v1.clones.activity.list(
            "cloneId",
        )
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.activity.with_raw_response.list(
            "cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ActivityListResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.activity.with_streaming_response.list(
            "cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ActivityListResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.activity.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloneforce) -> None:
        activity = await async_client.v1.clones.activity.delete(
            activity_id="activityId",
            clone_id="cloneId",
        )
        assert_matches_type(ActivityDeleteResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.activity.with_raw_response.delete(
            activity_id="activityId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(ActivityDeleteResponse, activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.activity.with_streaming_response.delete(
            activity_id="activityId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(ActivityDeleteResponse, activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.activity.with_raw_response.delete(
                activity_id="activityId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `activity_id` but received ''"):
            await async_client.v1.clones.activity.with_raw_response.delete(
                activity_id="",
                clone_id="cloneId",
            )
