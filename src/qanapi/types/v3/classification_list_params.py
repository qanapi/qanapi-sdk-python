# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["ClassificationListParams"]


class ClassificationListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]

    per_page: int

    providers: Iterable[int]

    roles: Iterable[int]

    search: str

    sort: str

    user: int
