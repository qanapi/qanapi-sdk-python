# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..api_key import APIKey
from ..._models import BaseModel

__all__ = ["LogAPIResponse", "Data", "Link"]


class Data(BaseModel):
    api_key: Optional[APIKey] = None

    api_key_id: Optional[int] = None

    configuration_id: Optional[int] = None

    created_at: Optional[datetime] = None

    domain: Optional[str] = None

    endpoint: Optional[str] = None

    method: Optional[str] = None

    proxied: Optional[bool] = None

    proxied_to: Optional[str] = None

    request_id: Optional[str] = None

    status_code: Optional[int] = None


class Link(BaseModel):
    active: Optional[bool] = None

    label: Optional[str] = None

    page: Optional[int] = None

    url: Optional[str] = None


class LogAPIResponse(BaseModel):
    current_page: Optional[int] = None

    data: Optional[List[Data]] = None

    first_page_url: Optional[str] = None

    from_: Optional[int] = FieldInfo(alias="from", default=None)

    last_page: Optional[int] = None

    last_page_url: Optional[str] = None

    links: Optional[List[Link]] = None

    next_page_url: Optional[str] = None

    path: Optional[str] = None

    per_page: Optional[int] = None

    prev_page_url: Optional[str] = None

    to: Optional[int] = None

    total: Optional[int] = None
