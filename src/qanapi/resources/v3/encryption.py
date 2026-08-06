# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ...types.v3 import encryption_decrypt_params, encryption_encrypt_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v3.encryption_decrypt_response import EncryptionDecryptResponse
from ...types.v3.encryption_encrypt_response import EncryptionEncryptResponse

__all__ = ["EncryptionResource", "AsyncEncryptionResource"]


class EncryptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EncryptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EncryptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EncryptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return EncryptionResourceWithStreamingResponse(self)

    def decrypt(
        self,
        proxy: str,
        *,
        data: Dict[str, object],
        x_qanapi_fields: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EncryptionDecryptResponse:
        """Decrypt data

        Args:
          data: A JSON object to decrypt fields on.

        A maximum depth of 32 is allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy:
            raise ValueError(f"Expected a non-empty value for `proxy` but received {proxy!r}")
        extra_headers = {**strip_not_given({"x-qanapi-fields": x_qanapi_fields}), **(extra_headers or {})}
        return self._post(
            path_template("/v3/encryption/{proxy}/decrypt", proxy=proxy),
            body=maybe_transform(data, encryption_decrypt_params.EncryptionDecryptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EncryptionDecryptResponse,
        )

    def encrypt(
        self,
        proxy: str,
        *,
        data: Dict[str, object],
        x_qanapi_fields: str,
        x_qanapi_destination: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EncryptionEncryptResponse:
        """Encrypt data

        Args:
          data: A JSON object to encrypt fields on.

        A maximum depth of 32 is allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy:
            raise ValueError(f"Expected a non-empty value for `proxy` but received {proxy!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-qanapi-fields": x_qanapi_fields,
                    "x-qanapi-destination": x_qanapi_destination,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v3/encryption/{proxy}/encrypt", proxy=proxy),
            body=maybe_transform(data, encryption_encrypt_params.EncryptionEncryptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EncryptionEncryptResponse,
        )


class AsyncEncryptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEncryptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEncryptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEncryptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return AsyncEncryptionResourceWithStreamingResponse(self)

    async def decrypt(
        self,
        proxy: str,
        *,
        data: Dict[str, object],
        x_qanapi_fields: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EncryptionDecryptResponse:
        """Decrypt data

        Args:
          data: A JSON object to decrypt fields on.

        A maximum depth of 32 is allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy:
            raise ValueError(f"Expected a non-empty value for `proxy` but received {proxy!r}")
        extra_headers = {**strip_not_given({"x-qanapi-fields": x_qanapi_fields}), **(extra_headers or {})}
        return await self._post(
            path_template("/v3/encryption/{proxy}/decrypt", proxy=proxy),
            body=await async_maybe_transform(data, encryption_decrypt_params.EncryptionDecryptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EncryptionDecryptResponse,
        )

    async def encrypt(
        self,
        proxy: str,
        *,
        data: Dict[str, object],
        x_qanapi_fields: str,
        x_qanapi_destination: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EncryptionEncryptResponse:
        """Encrypt data

        Args:
          data: A JSON object to encrypt fields on.

        A maximum depth of 32 is allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not proxy:
            raise ValueError(f"Expected a non-empty value for `proxy` but received {proxy!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "x-qanapi-fields": x_qanapi_fields,
                    "x-qanapi-destination": x_qanapi_destination,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v3/encryption/{proxy}/encrypt", proxy=proxy),
            body=await async_maybe_transform(data, encryption_encrypt_params.EncryptionEncryptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EncryptionEncryptResponse,
        )


class EncryptionResourceWithRawResponse:
    def __init__(self, encryption: EncryptionResource) -> None:
        self._encryption = encryption

        self.decrypt = to_raw_response_wrapper(
            encryption.decrypt,
        )
        self.encrypt = to_raw_response_wrapper(
            encryption.encrypt,
        )


class AsyncEncryptionResourceWithRawResponse:
    def __init__(self, encryption: AsyncEncryptionResource) -> None:
        self._encryption = encryption

        self.decrypt = async_to_raw_response_wrapper(
            encryption.decrypt,
        )
        self.encrypt = async_to_raw_response_wrapper(
            encryption.encrypt,
        )


class EncryptionResourceWithStreamingResponse:
    def __init__(self, encryption: EncryptionResource) -> None:
        self._encryption = encryption

        self.decrypt = to_streamed_response_wrapper(
            encryption.decrypt,
        )
        self.encrypt = to_streamed_response_wrapper(
            encryption.encrypt,
        )


class AsyncEncryptionResourceWithStreamingResponse:
    def __init__(self, encryption: AsyncEncryptionResource) -> None:
        self._encryption = encryption

        self.decrypt = async_to_streamed_response_wrapper(
            encryption.decrypt,
        )
        self.encrypt = async_to_streamed_response_wrapper(
            encryption.encrypt,
        )
