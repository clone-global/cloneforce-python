# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.clones import ChatCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Cloneforce) -> None:
        completion = client.v1.clones.chats.completions.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloneforce) -> None:
        completion = client.v1.clones.chats.completions.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=False,
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloneforce) -> None:
        response = client.v1.clones.chats.completions.with_raw_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloneforce) -> None:
        with client.v1.clones.chats.completions.with_streaming_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(ChatCompletionResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="chatId",
                clone_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="",
                clone_id="cloneId",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Cloneforce) -> None:
        completion_stream = client.v1.clones.chats.completions.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=True,
        )
        completion_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloneforce) -> None:
        response = client.v1.clones.chats.completions.with_raw_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloneforce) -> None:
        with client.v1.clones.chats.completions.with_streaming_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="chatId",
                clone_id="",
                message="message",
                stream=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="",
                clone_id="cloneId",
                message="message",
                stream=True,
            )


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloneforce) -> None:
        completion = await async_client.v1.clones.chats.completions.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloneforce) -> None:
        completion = await async_client.v1.clones.chats.completions.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=False,
        )
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.chats.completions.with_raw_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(ChatCompletionResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.chats.completions.with_streaming_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(ChatCompletionResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="chatId",
                clone_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="",
                clone_id="cloneId",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloneforce) -> None:
        completion_stream = await async_client.v1.clones.chats.completions.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=True,
        )
        await completion_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.chats.completions.with_raw_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.chats.completions.with_streaming_response.create(
            chat_id="chatId",
            clone_id="cloneId",
            message="message",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="chatId",
                clone_id="",
                message="message",
                stream=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.v1.clones.chats.completions.with_raw_response.create(
                chat_id="",
                clone_id="cloneId",
                message="message",
                stream=True,
            )
