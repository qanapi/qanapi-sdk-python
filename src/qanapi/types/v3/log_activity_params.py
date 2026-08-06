# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LogActivityParams"]


class LogActivityParams(TypedDict, total=False):
    log_name: Annotated[str, PropertyInfo(alias="logName")]

    page: int

    per_page: int

    user: int
    """User ID filter"""

    user_id: int
