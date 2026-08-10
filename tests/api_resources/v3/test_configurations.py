# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qanapi import Qanapi, AsyncQanapi
from tests.utils import assert_matches_type
from qanapi.types import Configuration
from qanapi.types.v3 import ConfigurationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Qanapi) -> None:
        configuration = client.v3.configurations.create(
            name="name",
            type="provider",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Qanapi) -> None:
        configuration = client.v3.configurations.create(
            name="name",
            type="provider",
            provider="google",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Qanapi) -> None:
        response = client.v3.configurations.with_raw_response.create(
            name="name",
            type="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Qanapi) -> None:
        with client.v3.configurations.with_streaming_response.create(
            name="name",
            type="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Qanapi) -> None:
        configuration = client.v3.configurations.update(
            configuration="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Qanapi) -> None:
        response = client.v3.configurations.with_raw_response.update(
            configuration="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Qanapi) -> None:
        with client.v3.configurations.with_streaming_response.update(
            configuration="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Qanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `configuration` but received ''"):
            client.v3.configurations.with_raw_response.update(
                configuration="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Qanapi) -> None:
        configuration = client.v3.configurations.list()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Qanapi) -> None:
        response = client.v3.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Qanapi) -> None:
        with client.v3.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Qanapi) -> None:
        configuration = client.v3.configurations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Qanapi) -> None:
        response = client.v3.configurations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Qanapi) -> None:
        with client.v3.configurations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Qanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `configuration` but received ''"):
            client.v3.configurations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_show(self, client: Qanapi) -> None:
        configuration = client.v3.configurations.show(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_show(self, client: Qanapi) -> None:
        response = client.v3.configurations.with_raw_response.show(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_show(self, client: Qanapi) -> None:
        with client.v3.configurations.with_streaming_response.show(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_show(self, client: Qanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `configuration` but received ''"):
            client.v3.configurations.with_raw_response.show(
                "",
            )


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncQanapi) -> None:
        configuration = await async_client.v3.configurations.create(
            name="name",
            type="provider",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncQanapi) -> None:
        configuration = await async_client.v3.configurations.create(
            name="name",
            type="provider",
            provider="google",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.configurations.with_raw_response.create(
            name="name",
            type="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.configurations.with_streaming_response.create(
            name="name",
            type="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncQanapi) -> None:
        configuration = await async_client.v3.configurations.update(
            configuration="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.configurations.with_raw_response.update(
            configuration="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.configurations.with_streaming_response.update(
            configuration="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncQanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `configuration` but received ''"):
            await async_client.v3.configurations.with_raw_response.update(
                configuration="",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncQanapi) -> None:
        configuration = await async_client.v3.configurations.list()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationListResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncQanapi) -> None:
        configuration = await async_client.v3.configurations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.configurations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.configurations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncQanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `configuration` but received ''"):
            await async_client.v3.configurations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_show(self, async_client: AsyncQanapi) -> None:
        configuration = await async_client.v3.configurations.show(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_show(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.configurations.with_raw_response.show(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(Configuration, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_show(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.configurations.with_streaming_response.show(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(Configuration, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_show(self, async_client: AsyncQanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `configuration` but received ''"):
            await async_client.v3.configurations.with_raw_response.show(
                "",
            )
