# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qanapi import Qanapi, AsyncQanapi
from tests.utils import assert_matches_type
from qanapi.types import APIKey
from qanapi.types.v3 import APIKeyListResponse, APIKeyRotateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Qanapi) -> None:
        api_key = client.v3.api_keys.list()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Qanapi) -> None:
        response = client.v3.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Qanapi) -> None:
        with client.v3.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Qanapi) -> None:
        api_key = client.v3.api_keys.revoke(
            0,
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Qanapi) -> None:
        response = client.v3.api_keys.with_raw_response.revoke(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Qanapi) -> None:
        with client.v3.api_keys.with_streaming_response.revoke(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate(self, client: Qanapi) -> None:
        api_key = client.v3.api_keys.rotate(
            0,
        )
        assert_matches_type(APIKeyRotateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate(self, client: Qanapi) -> None:
        response = client.v3.api_keys.with_raw_response.rotate(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyRotateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate(self, client: Qanapi) -> None:
        with client.v3.api_keys.with_streaming_response.rotate(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyRotateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_show(self, client: Qanapi) -> None:
        api_key = client.v3.api_keys.show(
            0,
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_show(self, client: Qanapi) -> None:
        response = client.v3.api_keys.with_raw_response.show(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_show(self, client: Qanapi) -> None:
        with client.v3.api_keys.with_streaming_response.show(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncQanapi) -> None:
        api_key = await async_client.v3.api_keys.list()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.api_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyListResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.api_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyListResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncQanapi) -> None:
        api_key = await async_client.v3.api_keys.revoke(
            0,
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.api_keys.with_raw_response.revoke(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.api_keys.with_streaming_response.revoke(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate(self, async_client: AsyncQanapi) -> None:
        api_key = await async_client.v3.api_keys.rotate(
            0,
        )
        assert_matches_type(APIKeyRotateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.api_keys.with_raw_response.rotate(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyRotateResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.api_keys.with_streaming_response.rotate(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyRotateResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_show(self, async_client: AsyncQanapi) -> None:
        api_key = await async_client.v3.api_keys.show(
            0,
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_show(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.api_keys.with_raw_response.show(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_show(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.api_keys.with_streaming_response.show(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
