# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.clones.skills import SkillConnectionInfo, ConnectionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cloneforce) -> None:
        connection = client.v1.clones.skills.connections.update(
            setting_name="settingName",
            clone_id="cloneId",
            skill_name="skillName",
            connection_id="connectionId",
        )
        assert_matches_type(SkillConnectionInfo, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cloneforce) -> None:
        response = client.v1.clones.skills.connections.with_raw_response.update(
            setting_name="settingName",
            clone_id="cloneId",
            skill_name="skillName",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(SkillConnectionInfo, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cloneforce) -> None:
        with client.v1.clones.skills.connections.with_streaming_response.update(
            setting_name="settingName",
            clone_id="cloneId",
            skill_name="skillName",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(SkillConnectionInfo, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.skills.connections.with_raw_response.update(
                setting_name="settingName",
                clone_id="",
                skill_name="skillName",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            client.v1.clones.skills.connections.with_raw_response.update(
                setting_name="settingName",
                clone_id="cloneId",
                skill_name="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_name` but received ''"):
            client.v1.clones.skills.connections.with_raw_response.update(
                setting_name="",
                clone_id="cloneId",
                skill_name="skillName",
                connection_id="connectionId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cloneforce) -> None:
        connection = client.v1.clones.skills.connections.list(
            skill_name="skillName",
            clone_id="cloneId",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cloneforce) -> None:
        response = client.v1.clones.skills.connections.with_raw_response.list(
            skill_name="skillName",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cloneforce) -> None:
        with client.v1.clones.skills.connections.with_streaming_response.list(
            skill_name="skillName",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.skills.connections.with_raw_response.list(
                skill_name="skillName",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            client.v1.clones.skills.connections.with_raw_response.list(
                skill_name="",
                clone_id="cloneId",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.clones.skills.connections.update(
            setting_name="settingName",
            clone_id="cloneId",
            skill_name="skillName",
            connection_id="connectionId",
        )
        assert_matches_type(SkillConnectionInfo, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.skills.connections.with_raw_response.update(
            setting_name="settingName",
            clone_id="cloneId",
            skill_name="skillName",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(SkillConnectionInfo, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.skills.connections.with_streaming_response.update(
            setting_name="settingName",
            clone_id="cloneId",
            skill_name="skillName",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(SkillConnectionInfo, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.skills.connections.with_raw_response.update(
                setting_name="settingName",
                clone_id="",
                skill_name="skillName",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            await async_client.v1.clones.skills.connections.with_raw_response.update(
                setting_name="settingName",
                clone_id="cloneId",
                skill_name="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `setting_name` but received ''"):
            await async_client.v1.clones.skills.connections.with_raw_response.update(
                setting_name="",
                clone_id="cloneId",
                skill_name="skillName",
                connection_id="connectionId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloneforce) -> None:
        connection = await async_client.v1.clones.skills.connections.list(
            skill_name="skillName",
            clone_id="cloneId",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.skills.connections.with_raw_response.list(
            skill_name="skillName",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.skills.connections.with_streaming_response.list(
            skill_name="skillName",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.skills.connections.with_raw_response.list(
                skill_name="skillName",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            await async_client.v1.clones.skills.connections.with_raw_response.list(
                skill_name="",
                clone_id="cloneId",
            )
