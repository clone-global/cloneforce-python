# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.clones import GenerationStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: Cloneforce) -> None:
        voice = client.v1.clones.voice.generate(
            clone_id="cloneId",
        )
        assert_matches_type(GenerationStatus, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_with_all_params(self, client: Cloneforce) -> None:
        voice = client.v1.clones.voice.generate(
            clone_id="cloneId",
            additional_instructions="additionalInstructions",
        )
        assert_matches_type(GenerationStatus, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: Cloneforce) -> None:
        response = client.v1.clones.voice.with_raw_response.generate(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(GenerationStatus, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: Cloneforce) -> None:
        with client.v1.clones.voice.with_streaming_response.generate(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(GenerationStatus, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.voice.with_raw_response.generate(
                clone_id="",
            )


class TestAsyncVoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncCloneforce) -> None:
        voice = await async_client.v1.clones.voice.generate(
            clone_id="cloneId",
        )
        assert_matches_type(GenerationStatus, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncCloneforce) -> None:
        voice = await async_client.v1.clones.voice.generate(
            clone_id="cloneId",
            additional_instructions="additionalInstructions",
        )
        assert_matches_type(GenerationStatus, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.voice.with_raw_response.generate(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(GenerationStatus, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.voice.with_streaming_response.generate(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(GenerationStatus, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.voice.with_raw_response.generate(
                clone_id="",
            )
