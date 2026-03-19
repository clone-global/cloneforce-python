# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce._utils import parse_datetime
from cloneforce.types.v1.clones import (
    TaskSummary,
    TaskListResponse,
    TaskDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
            color="color",
            is_recurring=True,
            recurrence={
                "interval": 0,
                "pattern": "Minutely",
                "ends_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cloneforce) -> None:
        response = client.v1.clones.tasks.with_raw_response.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cloneforce) -> None:
        with client.v1.clones.tasks.with_streaming_response.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskSummary, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.create(
                clone_id="",
                prompt="prompt",
                starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.retrieve(
            task_id="taskId",
            clone_id="cloneId",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cloneforce) -> None:
        response = client.v1.clones.tasks.with_raw_response.retrieve(
            task_id="taskId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cloneforce) -> None:
        with client.v1.clones.tasks.with_streaming_response.retrieve(
            task_id="taskId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskSummary, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.retrieve(
                task_id="taskId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.retrieve(
                task_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.update(
            task_id="taskId",
            clone_id="cloneId",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.update(
            task_id="taskId",
            clone_id="cloneId",
            color="color",
            is_recurring=True,
            prompt="prompt",
            recurrence={
                "interval": 0,
                "pattern": "Minutely",
                "ends_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cloneforce) -> None:
        response = client.v1.clones.tasks.with_raw_response.update(
            task_id="taskId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cloneforce) -> None:
        with client.v1.clones.tasks.with_streaming_response.update(
            task_id="taskId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskSummary, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.update(
                task_id="taskId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.update(
                task_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.list(
            clone_id="cloneId",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.list(
            clone_id="cloneId",
            is_recurring="true",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cloneforce) -> None:
        response = client.v1.clones.tasks.with_raw_response.list(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cloneforce) -> None:
        with client.v1.clones.tasks.with_streaming_response.list(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.list(
                clone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cloneforce) -> None:
        task = client.v1.clones.tasks.delete(
            task_id="taskId",
            clone_id="cloneId",
        )
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cloneforce) -> None:
        response = client.v1.clones.tasks.with_raw_response.delete(
            task_id="taskId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cloneforce) -> None:
        with client.v1.clones.tasks.with_streaming_response.delete(
            task_id="taskId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskDeleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.delete(
                task_id="taskId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.v1.clones.tasks.with_raw_response.delete(
                task_id="",
                clone_id="cloneId",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
            color="color",
            is_recurring=True,
            recurrence={
                "interval": 0,
                "pattern": "Minutely",
                "ends_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.tasks.with_raw_response.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.tasks.with_streaming_response.create(
            clone_id="cloneId",
            prompt="prompt",
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskSummary, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.create(
                clone_id="",
                prompt="prompt",
                starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                title="title",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.retrieve(
            task_id="taskId",
            clone_id="cloneId",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.tasks.with_raw_response.retrieve(
            task_id="taskId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.tasks.with_streaming_response.retrieve(
            task_id="taskId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskSummary, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.retrieve(
                task_id="taskId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.retrieve(
                task_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.update(
            task_id="taskId",
            clone_id="cloneId",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.update(
            task_id="taskId",
            clone_id="cloneId",
            color="color",
            is_recurring=True,
            prompt="prompt",
            recurrence={
                "interval": 0,
                "pattern": "Minutely",
                "ends_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            starts_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            title="title",
        )
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.tasks.with_raw_response.update(
            task_id="taskId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskSummary, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.tasks.with_streaming_response.update(
            task_id="taskId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskSummary, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.update(
                task_id="taskId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.update(
                task_id="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.list(
            clone_id="cloneId",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.list(
            clone_id="cloneId",
            is_recurring="true",
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.tasks.with_raw_response.list(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.tasks.with_streaming_response.list(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.list(
                clone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloneforce) -> None:
        task = await async_client.v1.clones.tasks.delete(
            task_id="taskId",
            clone_id="cloneId",
        )
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.tasks.with_raw_response.delete(
            task_id="taskId",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskDeleteResponse, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.tasks.with_streaming_response.delete(
            task_id="taskId",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskDeleteResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.delete(
                task_id="taskId",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.v1.clones.tasks.with_raw_response.delete(
                task_id="",
                clone_id="cloneId",
            )
