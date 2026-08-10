# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LogAPIParams"]


class LogAPIParams(TypedDict, total=False):
    api_key: Annotated[int, PropertyInfo(alias="apiKey")]
    """API Key ID filter"""

    page: int

    per_page: int
