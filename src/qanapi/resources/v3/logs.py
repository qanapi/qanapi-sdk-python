# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v3 import log_api_params, log_unified_params, log_activity_params, log_qanapi_flow_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v3.log_api_response import LogAPIResponse
from ...types.v3.log_unified_response import LogUnifiedResponse
from ...types.v3.log_activity_response import LogActivityResponse
from ...types.v3.log_qanapi_flow_response import LogQanapiFlowResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def activity(
        self,
        *,
        log_name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        user: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogActivityResponse:
        """
        Get activity logs

        Args:
          user: User ID filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/logs/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "log_name": log_name,
                        "page": page,
                        "per_page": per_page,
                        "user": user,
                        "user_id": user_id,
                    },
                    log_activity_params.LogActivityParams,
                ),
            ),
            cast_to=LogActivityResponse,
        )

    def api(
        self,
        *,
        api_key: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogAPIResponse:
        """
        Get API logs

        Args:
          api_key: API Key ID filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/logs/api",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "api_key": api_key,
                        "page": page,
                        "per_page": per_page,
                    },
                    log_api_params.LogAPIParams,
                ),
            ),
            cast_to=LogAPIResponse,
        )

    def qanapi_flow(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogQanapiFlowResponse:
        """
        Get Qanapi Flow logs

        Args:
          type: Integration type filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/logs/qanapi-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    log_qanapi_flow_params.LogQanapiFlowParams,
                ),
            ),
            cast_to=LogQanapiFlowResponse,
        )

    def unified(
        self,
        *,
        action: str | Omit = omit,
        causer_email: str | Omit = omit,
        description: str | Omit = omit,
        details: str | Omit = omit,
        log_type: Literal["activity", "api", "usage"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        request_id: str | Omit = omit,
        status_code: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogUnifiedResponse:
        """
        Get unified logs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/logs/unified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "causer_email": causer_email,
                        "description": description,
                        "details": details,
                        "log_type": log_type,
                        "page": page,
                        "per_page": per_page,
                        "request_id": request_id,
                        "status_code": status_code,
                        "user_id": user_id,
                    },
                    log_unified_params.LogUnifiedParams,
                ),
            ),
            cast_to=LogUnifiedResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/qanapi/qanapi-sdk-python#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def activity(
        self,
        *,
        log_name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        user: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogActivityResponse:
        """
        Get activity logs

        Args:
          user: User ID filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/logs/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "log_name": log_name,
                        "page": page,
                        "per_page": per_page,
                        "user": user,
                        "user_id": user_id,
                    },
                    log_activity_params.LogActivityParams,
                ),
            ),
            cast_to=LogActivityResponse,
        )

    async def api(
        self,
        *,
        api_key: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogAPIResponse:
        """
        Get API logs

        Args:
          api_key: API Key ID filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/logs/api",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "api_key": api_key,
                        "page": page,
                        "per_page": per_page,
                    },
                    log_api_params.LogAPIParams,
                ),
            ),
            cast_to=LogAPIResponse,
        )

    async def qanapi_flow(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogQanapiFlowResponse:
        """
        Get Qanapi Flow logs

        Args:
          type: Integration type filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/logs/qanapi-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    log_qanapi_flow_params.LogQanapiFlowParams,
                ),
            ),
            cast_to=LogQanapiFlowResponse,
        )

    async def unified(
        self,
        *,
        action: str | Omit = omit,
        causer_email: str | Omit = omit,
        description: str | Omit = omit,
        details: str | Omit = omit,
        log_type: Literal["activity", "api", "usage"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        request_id: str | Omit = omit,
        status_code: int | Omit = omit,
        user_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogUnifiedResponse:
        """
        Get unified logs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/logs/unified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "action": action,
                        "causer_email": causer_email,
                        "description": description,
                        "details": details,
                        "log_type": log_type,
                        "page": page,
                        "per_page": per_page,
                        "request_id": request_id,
                        "status_code": status_code,
                        "user_id": user_id,
                    },
                    log_unified_params.LogUnifiedParams,
                ),
            ),
            cast_to=LogUnifiedResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.activity = to_raw_response_wrapper(
            logs.activity,
        )
        self.api = to_raw_response_wrapper(
            logs.api,
        )
        self.qanapi_flow = to_raw_response_wrapper(
            logs.qanapi_flow,
        )
        self.unified = to_raw_response_wrapper(
            logs.unified,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.activity = async_to_raw_response_wrapper(
            logs.activity,
        )
        self.api = async_to_raw_response_wrapper(
            logs.api,
        )
        self.qanapi_flow = async_to_raw_response_wrapper(
            logs.qanapi_flow,
        )
        self.unified = async_to_raw_response_wrapper(
            logs.unified,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.activity = to_streamed_response_wrapper(
            logs.activity,
        )
        self.api = to_streamed_response_wrapper(
            logs.api,
        )
        self.qanapi_flow = to_streamed_response_wrapper(
            logs.qanapi_flow,
        )
        self.unified = to_streamed_response_wrapper(
            logs.unified,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.activity = async_to_streamed_response_wrapper(
            logs.activity,
        )
        self.api = async_to_streamed_response_wrapper(
            logs.api,
        )
        self.qanapi_flow = async_to_streamed_response_wrapper(
            logs.qanapi_flow,
        )
        self.unified = async_to_streamed_response_wrapper(
            logs.unified,
        )
