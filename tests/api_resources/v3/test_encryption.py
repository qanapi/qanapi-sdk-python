# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from qanapi import Qanapi, AsyncQanapi
from tests.utils import assert_matches_type
from qanapi.types.v3 import (
    EncryptionDecryptResponse,
    EncryptionEncryptResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEncryption:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_decrypt(self, client: Qanapi) -> None:
        encryption = client.v3.encryption.decrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )
        assert_matches_type(EncryptionDecryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_decrypt(self, client: Qanapi) -> None:
        response = client.v3.encryption.with_raw_response.decrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        encryption = response.parse()
        assert_matches_type(EncryptionDecryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_decrypt(self, client: Qanapi) -> None:
        with client.v3.encryption.with_streaming_response.decrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            encryption = response.parse()
            assert_matches_type(EncryptionDecryptResponse, encryption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_decrypt(self, client: Qanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy` but received ''"):
            client.v3.encryption.with_raw_response.decrypt(
                proxy="",
                data={
                    "name": "bar",
                    "email": "bar",
                    "ssn": "bar",
                    "dob": "bar",
                    "address": "bar",
                },
                x_qanapi_fields="x-qanapi-fields",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_encrypt(self, client: Qanapi) -> None:
        encryption = client.v3.encryption.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )
        assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_encrypt_with_all_params(self, client: Qanapi) -> None:
        encryption = client.v3.encryption.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
            x_qanapi_destination="x-qanapi-destination",
        )
        assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_encrypt(self, client: Qanapi) -> None:
        response = client.v3.encryption.with_raw_response.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        encryption = response.parse()
        assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_encrypt(self, client: Qanapi) -> None:
        with client.v3.encryption.with_streaming_response.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            encryption = response.parse()
            assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_encrypt(self, client: Qanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy` but received ''"):
            client.v3.encryption.with_raw_response.encrypt(
                proxy="",
                data={
                    "name": "bar",
                    "email": "bar",
                    "ssn": "bar",
                    "dob": "bar",
                    "address": "bar",
                },
                x_qanapi_fields="x-qanapi-fields",
            )


class TestAsyncEncryption:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_decrypt(self, async_client: AsyncQanapi) -> None:
        encryption = await async_client.v3.encryption.decrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )
        assert_matches_type(EncryptionDecryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_decrypt(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.encryption.with_raw_response.decrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        encryption = await response.parse()
        assert_matches_type(EncryptionDecryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_decrypt(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.encryption.with_streaming_response.decrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            encryption = await response.parse()
            assert_matches_type(EncryptionDecryptResponse, encryption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_decrypt(self, async_client: AsyncQanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy` but received ''"):
            await async_client.v3.encryption.with_raw_response.decrypt(
                proxy="",
                data={
                    "name": "bar",
                    "email": "bar",
                    "ssn": "bar",
                    "dob": "bar",
                    "address": "bar",
                },
                x_qanapi_fields="x-qanapi-fields",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_encrypt(self, async_client: AsyncQanapi) -> None:
        encryption = await async_client.v3.encryption.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )
        assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_encrypt_with_all_params(self, async_client: AsyncQanapi) -> None:
        encryption = await async_client.v3.encryption.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
            x_qanapi_destination="x-qanapi-destination",
        )
        assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_encrypt(self, async_client: AsyncQanapi) -> None:
        response = await async_client.v3.encryption.with_raw_response.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        encryption = await response.parse()
        assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_encrypt(self, async_client: AsyncQanapi) -> None:
        async with async_client.v3.encryption.with_streaming_response.encrypt(
            proxy="proxy",
            data={
                "name": "bar",
                "email": "bar",
                "ssn": "bar",
                "dob": "bar",
                "address": "bar",
            },
            x_qanapi_fields="x-qanapi-fields",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            encryption = await response.parse()
            assert_matches_type(EncryptionEncryptResponse, encryption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_encrypt(self, async_client: AsyncQanapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy` but received ''"):
            await async_client.v3.encryption.with_raw_response.encrypt(
                proxy="",
                data={
                    "name": "bar",
                    "email": "bar",
                    "ssn": "bar",
                    "dob": "bar",
                    "address": "bar",
                },
                x_qanapi_fields="x-qanapi-fields",
            )
