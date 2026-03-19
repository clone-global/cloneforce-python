# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloneforce import Cloneforce, AsyncCloneforce
from tests.utils import assert_matches_type
from cloneforce._utils import parse_datetime
from cloneforce.types.v1.clones import CloneProfile

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cloneforce) -> None:
        profile = client.v1.clones.profile.list(
            "cloneId",
        )
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cloneforce) -> None:
        response = client.v1.clones.profile.with_raw_response.list(
            "cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cloneforce) -> None:
        with client.v1.clones.profile.with_streaming_response.list(
            "cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(CloneProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.profile.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all(self, client: Cloneforce) -> None:
        profile = client.v1.clones.profile.patch_all(
            clone_id="cloneId",
        )
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all_with_all_params(self, client: Cloneforce) -> None:
        profile = client.v1.clones.profile.patch_all(
            clone_id="cloneId",
            appearance_desc="appearanceDesc",
            birthdate=parse_datetime("2019-12-27T18:11:19.117Z"),
            career_desc="careerDesc",
            childhood_desc="childhoodDesc",
            current_city="currentCity",
            education_desc="educationDesc",
            family_desc="familyDesc",
            finances_desc="financesDesc",
            gender="gender",
            hometown="hometown",
            interests_desc="interestsDesc",
            is_enabled=True,
            language="language",
            lifestyle_desc="lifestyleDesc",
            marital_status="maritalStatus",
            name="name",
            nationality="nationality",
            occupation="occupation",
            principles_desc="principlesDesc",
            races=["string"],
            screen_name="screenName",
            social_circle_desc="socialCircleDesc",
            social_hobbies_desc="socialHobbiesDesc",
            sports_desc="sportsDesc",
            travel_desc="travelDesc",
            unusual_hobbies_desc="unusualHobbiesDesc",
        )
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_all(self, client: Cloneforce) -> None:
        response = client.v1.clones.profile.with_raw_response.patch_all(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_all(self, client: Cloneforce) -> None:
        with client.v1.clones.profile.with_streaming_response.patch_all(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(CloneProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch_all(self, client: Cloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            client.v1.clones.profile.with_raw_response.patch_all(
                clone_id="",
            )


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloneforce) -> None:
        profile = await async_client.v1.clones.profile.list(
            "cloneId",
        )
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.profile.with_raw_response.list(
            "cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.profile.with_streaming_response.list(
            "cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(CloneProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.profile.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all(self, async_client: AsyncCloneforce) -> None:
        profile = await async_client.v1.clones.profile.patch_all(
            clone_id="cloneId",
        )
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all_with_all_params(self, async_client: AsyncCloneforce) -> None:
        profile = await async_client.v1.clones.profile.patch_all(
            clone_id="cloneId",
            appearance_desc="appearanceDesc",
            birthdate=parse_datetime("2019-12-27T18:11:19.117Z"),
            career_desc="careerDesc",
            childhood_desc="childhoodDesc",
            current_city="currentCity",
            education_desc="educationDesc",
            family_desc="familyDesc",
            finances_desc="financesDesc",
            gender="gender",
            hometown="hometown",
            interests_desc="interestsDesc",
            is_enabled=True,
            language="language",
            lifestyle_desc="lifestyleDesc",
            marital_status="maritalStatus",
            name="name",
            nationality="nationality",
            occupation="occupation",
            principles_desc="principlesDesc",
            races=["string"],
            screen_name="screenName",
            social_circle_desc="socialCircleDesc",
            social_hobbies_desc="socialHobbiesDesc",
            sports_desc="sportsDesc",
            travel_desc="travelDesc",
            unusual_hobbies_desc="unusualHobbiesDesc",
        )
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_all(self, async_client: AsyncCloneforce) -> None:
        response = await async_client.v1.clones.profile.with_raw_response.patch_all(
            clone_id="cloneId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(CloneProfile, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_all(self, async_client: AsyncCloneforce) -> None:
        async with async_client.v1.clones.profile.with_streaming_response.patch_all(
            clone_id="cloneId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(CloneProfile, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch_all(self, async_client: AsyncCloneforce) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `clone_id` but received ''"):
            await async_client.v1.clones.profile.with_raw_response.patch_all(
                clone_id="",
            )
