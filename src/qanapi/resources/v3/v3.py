# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from .roles import (
    RolesResource,
    AsyncRolesResource,
    RolesResourceWithRawResponse,
    AsyncRolesResourceWithRawResponse,
    RolesResourceWithStreamingResponse,
    AsyncRolesResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
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
from .encryption import (
    EncryptionResource,
    AsyncEncryptionResource,
    EncryptionResourceWithRawResponse,
    AsyncEncryptionResourceWithRawResponse,
    EncryptionResourceWithStreamingResponse,
    AsyncEncryptionResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .configurations import (
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from .classifications import (
    ClassificationsResource,
    AsyncClassificationsResource,
    ClassificationsResourceWithRawResponse,
    AsyncClassificationsResourceWithRawResponse,
    ClassificationsResourceWithStreamingResponse,
    AsyncClassificationsResourceWithStreamingResponse,
)

__all__ = ["V3Resource", "AsyncV3Resource"]


class V3Resource(SyncAPIResource):
    @cached_property
    def roles(self) -> RolesResource:
        return RolesResource(self._client)

    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def encryption(self) -> EncryptionResource:
        return EncryptionResource(self._client)

    @cached_property
    def classifications(self) -> ClassificationsResource:
        return ClassificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return V3ResourceWithStreamingResponse(self)


class AsyncV3Resource(AsyncAPIResource):
    @cached_property
    def roles(self) -> AsyncRolesResource:
        return AsyncRolesResource(self._client)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def encryption(self) -> AsyncEncryptionResource:
        return AsyncEncryptionResource(self._client)

    @cached_property
    def classifications(self) -> AsyncClassificationsResource:
        return AsyncClassificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return AsyncV3ResourceWithStreamingResponse(self)


class V3ResourceWithRawResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

    @cached_property
    def roles(self) -> RolesResourceWithRawResponse:
        return RolesResourceWithRawResponse(self._v3.roles)

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._v3.configurations)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._v3.users)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._v3.api_keys)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._v3.logs)

    @cached_property
    def encryption(self) -> EncryptionResourceWithRawResponse:
        return EncryptionResourceWithRawResponse(self._v3.encryption)

    @cached_property
    def classifications(self) -> ClassificationsResourceWithRawResponse:
        return ClassificationsResourceWithRawResponse(self._v3.classifications)


class AsyncV3ResourceWithRawResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

    @cached_property
    def roles(self) -> AsyncRolesResourceWithRawResponse:
        return AsyncRolesResourceWithRawResponse(self._v3.roles)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._v3.configurations)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._v3.users)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._v3.api_keys)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._v3.logs)

    @cached_property
    def encryption(self) -> AsyncEncryptionResourceWithRawResponse:
        return AsyncEncryptionResourceWithRawResponse(self._v3.encryption)

    @cached_property
    def classifications(self) -> AsyncClassificationsResourceWithRawResponse:
        return AsyncClassificationsResourceWithRawResponse(self._v3.classifications)


class V3ResourceWithStreamingResponse:
    def __init__(self, v3: V3Resource) -> None:
        self._v3 = v3

    @cached_property
    def roles(self) -> RolesResourceWithStreamingResponse:
        return RolesResourceWithStreamingResponse(self._v3.roles)

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._v3.configurations)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._v3.users)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._v3.api_keys)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._v3.logs)

    @cached_property
    def encryption(self) -> EncryptionResourceWithStreamingResponse:
        return EncryptionResourceWithStreamingResponse(self._v3.encryption)

    @cached_property
    def classifications(self) -> ClassificationsResourceWithStreamingResponse:
        return ClassificationsResourceWithStreamingResponse(self._v3.classifications)


class AsyncV3ResourceWithStreamingResponse:
    def __init__(self, v3: AsyncV3Resource) -> None:
        self._v3 = v3

    @cached_property
    def roles(self) -> AsyncRolesResourceWithStreamingResponse:
        return AsyncRolesResourceWithStreamingResponse(self._v3.roles)

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._v3.configurations)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._v3.users)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._v3.api_keys)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._v3.logs)

    @cached_property
    def encryption(self) -> AsyncEncryptionResourceWithStreamingResponse:
        return AsyncEncryptionResourceWithStreamingResponse(self._v3.encryption)

    @cached_property
    def classifications(self) -> AsyncClassificationsResourceWithStreamingResponse:
        return AsyncClassificationsResourceWithStreamingResponse(self._v3.classifications)
