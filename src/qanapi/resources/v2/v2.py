# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from .decrypt import (
    DecryptResource,
    AsyncDecryptResource,
    DecryptResourceWithRawResponse,
    AsyncDecryptResourceWithRawResponse,
    DecryptResourceWithStreamingResponse,
    AsyncDecryptResourceWithStreamingResponse,
)
from .encrypt import (
    EncryptResource,
    AsyncEncryptResource,
    EncryptResourceWithRawResponse,
    AsyncEncryptResourceWithRawResponse,
    EncryptResourceWithStreamingResponse,
    AsyncEncryptResourceWithStreamingResponse,
)
from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def encrypt(self) -> EncryptResource:
        return EncryptResource(self._client)

    @cached_property
    def decrypt(self) -> DecryptResource:
        return DecryptResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def encrypt(self) -> AsyncEncryptResource:
        return AsyncEncryptResource(self._client)

    @cached_property
    def decrypt(self) -> AsyncDecryptResource:
        return AsyncDecryptResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._v2.auth)

    @cached_property
    def encrypt(self) -> EncryptResourceWithRawResponse:
        return EncryptResourceWithRawResponse(self._v2.encrypt)

    @cached_property
    def decrypt(self) -> DecryptResourceWithRawResponse:
        return DecryptResourceWithRawResponse(self._v2.decrypt)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._v2.api_keys)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._v2.auth)

    @cached_property
    def encrypt(self) -> AsyncEncryptResourceWithRawResponse:
        return AsyncEncryptResourceWithRawResponse(self._v2.encrypt)

    @cached_property
    def decrypt(self) -> AsyncDecryptResourceWithRawResponse:
        return AsyncDecryptResourceWithRawResponse(self._v2.decrypt)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._v2.api_keys)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._v2.auth)

    @cached_property
    def encrypt(self) -> EncryptResourceWithStreamingResponse:
        return EncryptResourceWithStreamingResponse(self._v2.encrypt)

    @cached_property
    def decrypt(self) -> DecryptResourceWithStreamingResponse:
        return DecryptResourceWithStreamingResponse(self._v2.decrypt)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._v2.api_keys)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._v2.auth)

    @cached_property
    def encrypt(self) -> AsyncEncryptResourceWithStreamingResponse:
        return AsyncEncryptResourceWithStreamingResponse(self._v2.encrypt)

    @cached_property
    def decrypt(self) -> AsyncDecryptResourceWithStreamingResponse:
        return AsyncDecryptResourceWithStreamingResponse(self._v2.decrypt)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._v2.api_keys)
