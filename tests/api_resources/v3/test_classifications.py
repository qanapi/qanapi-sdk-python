# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qanapi import Qanapi, AsyncQanapi
from tests.utils import assert_matches_type
from qanapi.types.v3 import (
    ClassificationListResponse,
    ClassificationShowResponse,
    ClassificationCreateResponse,
    ClassificationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qanapi) -> None:
        classification = client.v3.classifications.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qanapi) -> None:
        classification = client.v3.classifications.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
            description="description",
            emoji="emoji",
            gws_groups=[
                {
                    "id": "id",
                    "email": "email",
                    "name": "name",
                }
            ],
            provider_container_id=0,
            roles=[0],
            users=[0],
        )
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qanapi) -> None:
        response = client.v3.classifications.with_raw_response.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = response.parse()
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qanapi) -> None:
        with client.v3.classifications.with_streaming_response.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = response.parse()
            assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Qanapi) -> None:
        classification = client.v3.classifications.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Qanapi) -> None:
        classification = client.v3.classifications.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
            description="description",
            emoji="emoji",
            gws_groups=[
                {
                    "id": "id",
                    "email": "email",
                    "name": "name",
                }
            ],
            provider_container_id=0,
            roles=[0],
            users=[0],
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Qanapi) -> None:
        response = client.v3.classifications.with_raw_response.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = response.parse()
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Qanapi) -> None:
        with client.v3.classifications.with_streaming_response.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = response.parse()
            assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Qanapi) -> None:
        classification = client.v3.classifications.list()
        assert_matches_type(ClassificationListResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Qanapi) -> None:
        classification = client.v3.classifications.list(
            direction="asc",
            per_page=0,
            providers=[0],
            roles=[0],
            search="search",
            sort="sort",
            user=0,
        )
        assert_matches_type(ClassificationListResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Qanapi) -> None:
        response = client.v3.classifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = response.parse()
        assert_matches_type(ClassificationListResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Qanapi) -> None:
        with client.v3.classifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = response.parse()
            assert_matches_type(ClassificationListResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Qanapi) -> None:
        classification = client.v3.classifications.delete(
            0,
        )
        assert classification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Qanapi) -> None:
        response = client.v3.classifications.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = response.parse()
        assert classification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Qanapi) -> None:
        with client.v3.classifications.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = response.parse()
            assert classification is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_show(self, client: Qanapi) -> None:
        classification = client.v3.classifications.show(
            0,
        )
        assert_matches_type(ClassificationShowResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_show(self, client: Qanapi) -> None:
        response = client.v3.classifications.with_raw_response.show(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = response.parse()
        assert_matches_type(ClassificationShowResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_show(self, client: Qanapi) -> None:
        with client.v3.classifications.with_streaming_response.show(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = response.parse()
            assert_matches_type(ClassificationShowResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
            description="description",
            emoji="emoji",
            gws_groups=[
                {
                    "id": "id",
                    "email": "email",
                    "name": "name",
                }
            ],
            provider_container_id=0,
            roles=[0],
            users=[0],
        )
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.classifications.with_raw_response.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = await response.parse()
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.classifications.with_streaming_response.create(
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = await response.parse()
            assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
            description="description",
            emoji="emoji",
            gws_groups=[
                {
                    "id": "id",
                    "email": "email",
                    "name": "name",
                }
            ],
            provider_container_id=0,
            roles=[0],
            users=[0],
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.classifications.with_raw_response.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = await response.parse()
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.classifications.with_streaming_response.update(
            classification=0,
            bg_color="#e1cb97",
            fg_color="#e1cb97",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = await response.parse()
            assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.list()
        assert_matches_type(ClassificationListResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.list(
            direction="asc",
            per_page=0,
            providers=[0],
            roles=[0],
            search="search",
            sort="sort",
            user=0,
        )
        assert_matches_type(ClassificationListResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.classifications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = await response.parse()
        assert_matches_type(ClassificationListResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.classifications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = await response.parse()
            assert_matches_type(ClassificationListResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.delete(
            0,
        )
        assert classification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.classifications.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = await response.parse()
        assert classification is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.classifications.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = await response.parse()
            assert classification is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_show(self, async_client: AsyncQanapi) -> None:
        classification = await async_client.v3.classifications.show(
            0,
        )
        assert_matches_type(ClassificationShowResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_show(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.classifications.with_raw_response.show(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = await response.parse()
        assert_matches_type(ClassificationShowResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_show(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.classifications.with_streaming_response.show(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = await response.parse()
            assert_matches_type(ClassificationShowResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True
