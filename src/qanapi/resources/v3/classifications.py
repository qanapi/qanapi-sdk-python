# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v3 import classification_list_params, classification_create_params, classification_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.google_group_param import GoogleGroupParam
from ...types.v3.classification_list_response import ClassificationListResponse
from ...types.v3.classification_show_response import ClassificationShowResponse
from ...types.v3.classification_create_response import ClassificationCreateResponse
from ...types.v3.classification_update_response import ClassificationUpdateResponse

__all__ = ["ClassificationsResource", "AsyncClassificationsResource"]


class ClassificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ClassificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return ClassificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bg_color: str,
        fg_color: str,
        name: str,
        description: Optional[str] | Omit = omit,
        emoji: Optional[str] | Omit = omit,
        gws_groups: Iterable[GoogleGroupParam] | Omit = omit,
        provider_container_id: int | Omit = omit,
        roles: Iterable[int] | Omit = omit,
        users: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationCreateResponse:
        """
        Create classification

        Args:
          provider_container_id: Required if gws_groups is provided.

          roles: Array of role IDs.

          users: Array of user IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/classifications",
            body=maybe_transform(
                {
                    "bg_color": bg_color,
                    "fg_color": fg_color,
                    "name": name,
                    "description": description,
                    "emoji": emoji,
                    "gws_groups": gws_groups,
                    "provider_container_id": provider_container_id,
                    "roles": roles,
                    "users": users,
                },
                classification_create_params.ClassificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationCreateResponse,
        )

    def update(
        self,
        classification: int,
        *,
        bg_color: str,
        fg_color: str,
        name: str,
        description: Optional[str] | Omit = omit,
        emoji: Optional[str] | Omit = omit,
        gws_groups: Iterable[GoogleGroupParam] | Omit = omit,
        provider_container_id: int | Omit = omit,
        roles: Iterable[int] | Omit = omit,
        users: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationUpdateResponse:
        """
        Update classification

        Args:
          provider_container_id: Required if gws_groups is provided.

          roles: Array of role IDs.

          users: Array of user IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/v3/classifications/{classification}", classification=classification),
            body=maybe_transform(
                {
                    "bg_color": bg_color,
                    "fg_color": fg_color,
                    "name": name,
                    "description": description,
                    "emoji": emoji,
                    "gws_groups": gws_groups,
                    "provider_container_id": provider_container_id,
                    "roles": roles,
                    "users": users,
                },
                classification_update_params.ClassificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationUpdateResponse,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        providers: Iterable[int] | Omit = omit,
        roles: Iterable[int] | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        user: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationListResponse:
        """
        List classifications

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/classifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "per_page": per_page,
                        "providers": providers,
                        "roles": roles,
                        "search": search,
                        "sort": sort,
                        "user": user,
                    },
                    classification_list_params.ClassificationListParams,
                ),
            ),
            cast_to=ClassificationListResponse,
        )

    def delete(
        self,
        classification: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete classification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v3/classifications/{classification}", classification=classification),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def show(
        self,
        classification: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationShowResponse:
        """
        Get classification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/v3/classifications/{classification}", classification=classification),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationShowResponse,
        )


class AsyncClassificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return AsyncClassificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bg_color: str,
        fg_color: str,
        name: str,
        description: Optional[str] | Omit = omit,
        emoji: Optional[str] | Omit = omit,
        gws_groups: Iterable[GoogleGroupParam] | Omit = omit,
        provider_container_id: int | Omit = omit,
        roles: Iterable[int] | Omit = omit,
        users: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationCreateResponse:
        """
        Create classification

        Args:
          provider_container_id: Required if gws_groups is provided.

          roles: Array of role IDs.

          users: Array of user IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/classifications",
            body=await async_maybe_transform(
                {
                    "bg_color": bg_color,
                    "fg_color": fg_color,
                    "name": name,
                    "description": description,
                    "emoji": emoji,
                    "gws_groups": gws_groups,
                    "provider_container_id": provider_container_id,
                    "roles": roles,
                    "users": users,
                },
                classification_create_params.ClassificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationCreateResponse,
        )

    async def update(
        self,
        classification: int,
        *,
        bg_color: str,
        fg_color: str,
        name: str,
        description: Optional[str] | Omit = omit,
        emoji: Optional[str] | Omit = omit,
        gws_groups: Iterable[GoogleGroupParam] | Omit = omit,
        provider_container_id: int | Omit = omit,
        roles: Iterable[int] | Omit = omit,
        users: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationUpdateResponse:
        """
        Update classification

        Args:
          provider_container_id: Required if gws_groups is provided.

          roles: Array of role IDs.

          users: Array of user IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/v3/classifications/{classification}", classification=classification),
            body=await async_maybe_transform(
                {
                    "bg_color": bg_color,
                    "fg_color": fg_color,
                    "name": name,
                    "description": description,
                    "emoji": emoji,
                    "gws_groups": gws_groups,
                    "provider_container_id": provider_container_id,
                    "roles": roles,
                    "users": users,
                },
                classification_update_params.ClassificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationUpdateResponse,
        )

    async def list(
        self,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        per_page: int | Omit = omit,
        providers: Iterable[int] | Omit = omit,
        roles: Iterable[int] | Omit = omit,
        search: str | Omit = omit,
        sort: str | Omit = omit,
        user: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationListResponse:
        """
        List classifications

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/classifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "per_page": per_page,
                        "providers": providers,
                        "roles": roles,
                        "search": search,
                        "sort": sort,
                        "user": user,
                    },
                    classification_list_params.ClassificationListParams,
                ),
            ),
            cast_to=ClassificationListResponse,
        )

    async def delete(
        self,
        classification: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete classification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/classifications/{classification}", classification=classification),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def show(
        self,
        classification: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationShowResponse:
        """
        Get classification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/v3/classifications/{classification}", classification=classification),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationShowResponse,
        )


class ClassificationsResourceWithRawResponse:
    def __init__(self, classifications: ClassificationsResource) -> None:
        self._classifications = classifications

        self.create = to_raw_response_wrapper(
            classifications.create,
        )
        self.update = to_raw_response_wrapper(
            classifications.update,
        )
        self.list = to_raw_response_wrapper(
            classifications.list,
        )
        self.delete = to_raw_response_wrapper(
            classifications.delete,
        )
        self.show = to_raw_response_wrapper(
            classifications.show,
        )


class AsyncClassificationsResourceWithRawResponse:
    def __init__(self, classifications: AsyncClassificationsResource) -> None:
        self._classifications = classifications

        self.create = async_to_raw_response_wrapper(
            classifications.create,
        )
        self.update = async_to_raw_response_wrapper(
            classifications.update,
        )
        self.list = async_to_raw_response_wrapper(
            classifications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            classifications.delete,
        )
        self.show = async_to_raw_response_wrapper(
            classifications.show,
        )


class ClassificationsResourceWithStreamingResponse:
    def __init__(self, classifications: ClassificationsResource) -> None:
        self._classifications = classifications

        self.create = to_streamed_response_wrapper(
            classifications.create,
        )
        self.update = to_streamed_response_wrapper(
            classifications.update,
        )
        self.list = to_streamed_response_wrapper(
            classifications.list,
        )
        self.delete = to_streamed_response_wrapper(
            classifications.delete,
        )
        self.show = to_streamed_response_wrapper(
            classifications.show,
        )


class AsyncClassificationsResourceWithStreamingResponse:
    def __init__(self, classifications: AsyncClassificationsResource) -> None:
        self._classifications = classifications

        self.create = async_to_streamed_response_wrapper(
            classifications.create,
        )
        self.update = async_to_streamed_response_wrapper(
            classifications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            classifications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            classifications.delete,
        )
        self.show = async_to_streamed_response_wrapper(
            classifications.show,
        )
