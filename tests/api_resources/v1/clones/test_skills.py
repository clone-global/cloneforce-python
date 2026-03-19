# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce.types.v1.clones import (
    SkillSummary,
    SkillListResponse,
    SkillDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cloneforce) -> None:
        skill = client.v1.clones.skills.create(
            clone_id="cloneId",
            skill_id="skillId",
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloneforce) -> None:
        skill = client.v1.clones.skills.create(
            clone_id="cloneId",
            skill_id="skillId",
            is_active=True,
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cloneforce) -> None:
        response = client.v1.clones.skills.with_raw_response.create(
            clone_id="cloneId",
            skill_id="skillId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cloneforce) -> None:
        with client.v1.clones.skills.with_streaming_response.create(
            clone_id="cloneId",
            skill_id="skillId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillSummary, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.skills.with_raw_response.create(
                clone_id="",
                skill_id="skillId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cloneforce) -> None:
        skill = client.v1.clones.skills.update(
            skill_name="skillName",
            clone_id="cloneId",
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloneforce) -> None:
        skill = client.v1.clones.skills.update(
            skill_name="skillName",
            clone_id="cloneId",
            is_active=True,
            settings=[
                {
                    "name": "name",
                    "connection_id": "connectionId",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cloneforce) -> None:
        response = client.v1.clones.skills.with_raw_response.update(
            skill_name="skillName",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cloneforce) -> None:
        with client.v1.clones.skills.with_streaming_response.update(
            skill_name="skillName",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillSummary, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.skills.with_raw_response.update(
                skill_name="skillName",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            client.v1.clones.skills.with_raw_response.update(
                skill_name="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cloneforce) -> None:
        skill = client.v1.clones.skills.list(
            clone_id="cloneId",
        )
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloneforce) -> None:
        skill = client.v1.clones.skills.list(
            clone_id="cloneId",
            active="true",
        )
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cloneforce) -> None:
        response = client.v1.clones.skills.with_raw_response.list(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cloneforce) -> None:
        with client.v1.clones.skills.with_streaming_response.list(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillListResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.skills.with_raw_response.list(
                clone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cloneforce) -> None:
        skill = client.v1.clones.skills.delete(
            skill_name="skillName",
            clone_id="cloneId",
        )
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cloneforce) -> None:
        response = client.v1.clones.skills.with_raw_response.delete(
            skill_name="skillName",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cloneforce) -> None:
        with client.v1.clones.skills.with_streaming_response.delete(
            skill_name="skillName",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillDeleteResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.skills.with_raw_response.delete(
                skill_name="skillName",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            client.v1.clones.skills.with_raw_response.delete(
                skill_name="",
                clone_id="cloneId",
            )


class TestAsyncSkills:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloneforce) -> None:
        skill = await async_client.v1.clones.skills.create(
            clone_id="cloneId",
            skill_id="skillId",
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloneforce) -> None:
        skill = await async_client.v1.clones.skills.create(
            clone_id="cloneId",
            skill_id="skillId",
            is_active=True,
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.skills.with_raw_response.create(
            clone_id="cloneId",
            skill_id="skillId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.skills.with_streaming_response.create(
            clone_id="cloneId",
            skill_id="skillId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillSummary, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.skills.with_raw_response.create(
                clone_id="",
                skill_id="skillId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloneforce) -> None:
        skill = await async_client.v1.clones.skills.update(
            skill_name="skillName",
            clone_id="cloneId",
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloneforce) -> None:
        skill = await async_client.v1.clones.skills.update(
            skill_name="skillName",
            clone_id="cloneId",
            is_active=True,
            settings=[
                {
                    "name": "name",
                    "connection_id": "connectionId",
                    "value": "value",
                }
            ],
        )
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.skills.with_raw_response.update(
            skill_name="skillName",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillSummary, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.skills.with_streaming_response.update(
            skill_name="skillName",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillSummary, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.skills.with_raw_response.update(
                skill_name="skillName",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            await async_client.v1.clones.skills.with_raw_response.update(
                skill_name="",
                clone_id="cloneId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloneforce) -> None:
        skill = await async_client.v1.clones.skills.list(
            clone_id="cloneId",
        )
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloneforce) -> None:
        skill = await async_client.v1.clones.skills.list(
            clone_id="cloneId",
            active="true",
        )
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.skills.with_raw_response.list(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillListResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.skills.with_streaming_response.list(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillListResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.skills.with_raw_response.list(
                clone_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloneforce) -> None:
        skill = await async_client.v1.clones.skills.delete(
            skill_name="skillName",
            clone_id="cloneId",
        )
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.skills.with_raw_response.delete(
            skill_name="skillName",
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.skills.with_streaming_response.delete(
            skill_name="skillName",
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillDeleteResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.skills.with_raw_response.delete(
                skill_name="skillName",
                clone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_name` but received ''"):
            await async_client.v1.clones.skills.with_raw_response.delete(
                skill_name="",
                clone_id="cloneId",
            )
