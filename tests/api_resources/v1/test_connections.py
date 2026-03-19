# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1 import (
    OAuthProvision,
    ConnectionDetail,
    ConnectionStatus,
    ConnectionListResponse,
    ConnectionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cloneforce) -> None:
        connection = client.v1.connections.create(
            key="key",
            name="name",
            value="value",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.create(
            key="key",
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.create(
            key="key",
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionDetail, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cloneforce) -> None:
        connection = client.v1.connections.retrieve(
            "connectionId",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.retrieve(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.retrieve(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionDetail, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cloneforce) -> None:
        connection = client.v1.connections.update(
            connection_id="connectionId",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloneforce) -> None:
        connection = client.v1.connections.update(
            connection_id="connectionId",
            key="key",
            name="name",
            value="value",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.update(
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.update(
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionDetail, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.update(
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cloneforce) -> None:
        connection = client.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloneforce) -> None:
        connection = client.v1.connections.list(
            type="type",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cloneforce) -> None:
        connection = client.v1.connections.delete(
            "connectionId",
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.delete(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.delete(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_oauth(self, client: Cloneforce) -> None:
        connection = client.v1.connections.create_oauth(
            name="name",
            setting_type="settingType",
        )
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_oauth_with_all_params(self, client: Cloneforce) -> None:
        connection = client.v1.connections.create_oauth(
            name="name",
            setting_type="settingType",
            scopes=["string"],
        )
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_oauth(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.create_oauth(
            name="name",
            setting_type="settingType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_oauth(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.create_oauth(
            name="name",
            setting_type="settingType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(OAuthProvision, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Cloneforce) -> None:
        connection = client.v1.connections.get_status(
            "connectionId",
        )
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.get_status(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.get_status(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionStatus, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh(self, client: Cloneforce) -> None:
        connection = client.v1.connections.refresh(
            "connectionId",
        )
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.refresh(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.refresh(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionStatus, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_refresh(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.refresh(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reprovision_oauth(self, client: Cloneforce) -> None:
        connection = client.v1.connections.reprovision_oauth(
            "connectionId",
        )
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reprovision_oauth(self, client: Cloneforce) -> None:
        response = client.v1.connections.with_raw_response.reprovision_oauth(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reprovision_oauth(self, client: Cloneforce) -> None:
        with client.v1.connections.with_streaming_response.reprovision_oauth(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(OAuthProvision, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reprovision_oauth(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.v1.connections.with_raw_response.reprovision_oauth(
                "",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.create(
            key="key",
            name="name",
            value="value",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.create(
            key="key",
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.create(
            key="key",
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionDetail, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.retrieve(
            "connectionId",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.retrieve(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.retrieve(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionDetail, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.update(
            connection_id="connectionId",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.update(
            connection_id="connectionId",
            key="key",
            name="name",
            value="value",
        )
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.update(
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionDetail, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.update(
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionDetail, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.update(
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.list(
            type="type",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.delete(
            "connectionId",
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.delete(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.delete(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_oauth(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.create_oauth(
            name="name",
            setting_type="settingType",
        )
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_oauth_with_all_params(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.create_oauth(
            name="name",
            setting_type="settingType",
            scopes=["string"],
        )
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_oauth(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.create_oauth(
            name="name",
            setting_type="settingType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_oauth(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.create_oauth(
            name="name",
            setting_type="settingType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(OAuthProvision, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.get_status(
            "connectionId",
        )
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.get_status(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.get_status(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionStatus, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.refresh(
            "connectionId",
        )
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.refresh(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionStatus, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.refresh(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionStatus, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.refresh(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reprovision_oauth(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.connections.reprovision_oauth(
            "connectionId",
        )
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reprovision_oauth(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.connections.with_raw_response.reprovision_oauth(
            "connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(OAuthProvision, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reprovision_oauth(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.connections.with_streaming_response.reprovision_oauth(
            "connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(OAuthProvision, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reprovision_oauth(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.v1.connections.with_raw_response.reprovision_oauth(
                "",
            )
