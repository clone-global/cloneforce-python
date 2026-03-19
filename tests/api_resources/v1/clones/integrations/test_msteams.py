# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.clones.integrations import MsteamTeamsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMsteams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_teams(self, client: Cloneforce) -> None:
        msteam = client.v1.clones.integrations.msteams.teams(
            integration_id="integrationId",
            clone_id="cloneId",
            team_id="teamId",
        )
        assert_matches_type(MsteamTeamsResponse, msteam, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_teams(self, client: Cloneforce) -> None:
        response = client.v1.clones.integrations.msteams.with_raw_response.teams(
            integration_id="integrationId",
            clone_id="cloneId",
            team_id="teamId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        msteam = response.parse()
        assert_matches_type(MsteamTeamsResponse, msteam, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_teams(self, client: Cloneforce) -> None:
        with client.v1.clones.integrations.msteams.with_streaming_response.teams(
            integration_id="integrationId",
            clone_id="cloneId",
            team_id="teamId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            msteam = response.parse()
            assert_matches_type(MsteamTeamsResponse, msteam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_teams(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.integrations.msteams.with_raw_response.teams(
                integration_id="integrationId",
                clone_id="",
                team_id="teamId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.v1.clones.integrations.msteams.with_raw_response.teams(
                integration_id="",
                clone_id="cloneId",
                team_id="teamId",
            )


class TestAsyncMsteams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_teams(self, async_client: AsyncCloneforce) -> None:
        msteam = await async_client.v1.clones.integrations.msteams.teams(
            integration_id="integrationId",
            clone_id="cloneId",
            team_id="teamId",
        )
        assert_matches_type(MsteamTeamsResponse, msteam, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_teams(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.integrations.msteams.with_raw_response.teams(
            integration_id="integrationId",
            clone_id="cloneId",
            team_id="teamId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        msteam = await response.parse()
        assert_matches_type(MsteamTeamsResponse, msteam, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_teams(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.integrations.msteams.with_streaming_response.teams(
            integration_id="integrationId",
            clone_id="cloneId",
            team_id="teamId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            msteam = await response.parse()
            assert_matches_type(MsteamTeamsResponse, msteam, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_teams(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.integrations.msteams.with_raw_response.teams(
                integration_id="integrationId",
                clone_id="",
                team_id="teamId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.v1.clones.integrations.msteams.with_raw_response.teams(
                integration_id="",
                clone_id="cloneId",
                team_id="teamId",
            )
