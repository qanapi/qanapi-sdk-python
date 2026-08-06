# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qanapi import Qanapi, AsyncQanapi
from tests.utils import assert_matches_type
from qanapi.types.v3 import (
    LogAPIResponse,
    LogUnifiedResponse,
    LogActivityResponse,
    LogQanapiFlowResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activity(self, client: Qanapi) -> None:
        log = client.v3.logs.activity()
        assert_matches_type(LogActivityResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activity_with_all_params(self, client: Qanapi) -> None:
        log = client.v3.logs.activity(
            log_name="logName",
            page=0,
            per_page=0,
            user=0,
            user_id=0,
        )
        assert_matches_type(LogActivityResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_activity(self, client: Qanapi) -> None:
        response = client.v3.logs.with_raw_response.activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogActivityResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_activity(self, client: Qanapi) -> None:
        with client.v3.logs.with_streaming_response.activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogActivityResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_api(self, client: Qanapi) -> None:
        log = client.v3.logs.api()
        assert_matches_type(LogAPIResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_api_with_all_params(self, client: Qanapi) -> None:
        log = client.v3.logs.api(
            api_key=0,
            page=0,
            per_page=0,
        )
        assert_matches_type(LogAPIResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_api(self, client: Qanapi) -> None:
        response = client.v3.logs.with_raw_response.api()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogAPIResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_api(self, client: Qanapi) -> None:
        with client.v3.logs.with_streaming_response.api() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogAPIResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_qanapi_flow(self, client: Qanapi) -> None:
        log = client.v3.logs.qanapi_flow()
        assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_qanapi_flow_with_all_params(self, client: Qanapi) -> None:
        log = client.v3.logs.qanapi_flow(
            page=0,
            per_page=0,
            type="type",
        )
        assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_qanapi_flow(self, client: Qanapi) -> None:
        response = client.v3.logs.with_raw_response.qanapi_flow()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_qanapi_flow(self, client: Qanapi) -> None:
        with client.v3.logs.with_streaming_response.qanapi_flow() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unified(self, client: Qanapi) -> None:
        log = client.v3.logs.unified()
        assert_matches_type(LogUnifiedResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unified_with_all_params(self, client: Qanapi) -> None:
        log = client.v3.logs.unified(
            action="action",
            causer_email="causer_email",
            description="description",
            details="details",
            log_type="activity",
            page=0,
            per_page=0,
            request_id="request_id",
            status_code=0,
            user_id=0,
        )
        assert_matches_type(LogUnifiedResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unified(self, client: Qanapi) -> None:
        response = client.v3.logs.with_raw_response.unified()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogUnifiedResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unified(self, client: Qanapi) -> None:
        with client.v3.logs.with_streaming_response.unified() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogUnifiedResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activity(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.activity()
        assert_matches_type(LogActivityResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activity_with_all_params(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.activity(
            log_name="logName",
            page=0,
            per_page=0,
            user=0,
            user_id=0,
        )
        assert_matches_type(LogActivityResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_activity(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.logs.with_raw_response.activity()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogActivityResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_activity(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.logs.with_streaming_response.activity() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogActivityResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_api(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.api()
        assert_matches_type(LogAPIResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_api_with_all_params(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.api(
            api_key=0,
            page=0,
            per_page=0,
        )
        assert_matches_type(LogAPIResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_api(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.logs.with_raw_response.api()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogAPIResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_api(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.logs.with_streaming_response.api() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogAPIResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_qanapi_flow(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.qanapi_flow()
        assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_qanapi_flow_with_all_params(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.qanapi_flow(
            page=0,
            per_page=0,
            type="type",
        )
        assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_qanapi_flow(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.logs.with_raw_response.qanapi_flow()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_qanapi_flow(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.logs.with_streaming_response.qanapi_flow() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogQanapiFlowResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unified(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.unified()
        assert_matches_type(LogUnifiedResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unified_with_all_params(self, async_client: AsyncQanapi) -> None:
        log = await async_client.v3.logs.unified(
            action="action",
            causer_email="causer_email",
            description="description",
            details="details",
            log_type="activity",
            page=0,
            per_page=0,
            request_id="request_id",
            status_code=0,
            user_id=0,
        )
        assert_matches_type(LogUnifiedResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unified(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.logs.with_raw_response.unified()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogUnifiedResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unified(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.logs.with_streaming_response.unified() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogUnifiedResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True
