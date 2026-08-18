# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..google_group_param import GoogleGroupParam

__all__ = ["ClassificationCreateParams"]


class ClassificationCreateParams(TypedDict, total=False):
    bg_color: Required[str]

    fg_color: Required[str]

    name: Required[str]

    description: Optional[str]

    emoji: Optional[str]

    gws_groups: Iterable[GoogleGroupParam]

    provider_container_id: int
    """Required if gws_groups is provided."""

    roles: Iterable[int]
    """Array of role IDs."""

    users: Iterable[int]
    """Array of user IDs."""
