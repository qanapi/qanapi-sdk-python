# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LogUnifiedParams"]


class LogUnifiedParams(TypedDict, total=False):
    action: str

    causer_email: str

    description: str

    details: str

    log_type: Literal["activity", "api", "usage"]

    page: int

    per_page: int

    request_id: str

    status_code: int

    user_id: int
