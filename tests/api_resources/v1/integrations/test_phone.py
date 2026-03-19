# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.integrations import PhoneListAvailableResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_available(self, client: Cloneforce) -> None:
        phone = client.v1.integrations.phone.list_available()
        assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_available_with_all_params(self, client: Cloneforce) -> None:
        phone = client.v1.integrations.phone.list_available(
            area_code=0,
            country="country",
            limit=0,
        )
        assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_available(self, client: Cloneforce) -> None:
        response = client.v1.integrations.phone.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = response.parse()
        assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_available(self, client: Cloneforce) -> None:
        with client.v1.integrations.phone.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = response.parse()
            assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhone:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_available(self, async_client: AsyncCloneforce) -> None:
        phone = await async_client.v1.integrations.phone.list_available()
        assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_available_with_all_params(self, async_client: AsyncCloneforce) -> None:
        phone = await async_client.v1.integrations.phone.list_available(
            area_code=0,
            country="country",
            limit=0,
        )
        assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_available(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.integrations.phone.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone = await response.parse()
        assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_available(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.integrations.phone.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone = await response.parse()
            assert_matches_type(PhoneListAvailableResponse, phone, path=["response"])

        assert cast(Any, response.is_closed) is True
