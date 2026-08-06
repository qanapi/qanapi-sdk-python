# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "LogAPIResponse",
    "Data",
    "DataAPIKey",
    "DataAPIKeyConfiguration",
    "DataAPIKeyConfigurationValue",
    "DataAPIKeyPermission",
    "DataAPIKeyUser",
    "DataAPIKeyUserRole",
    "DataAPIKeyUserRolePermission",
    "Link",
]


class DataAPIKeyConfigurationValue(BaseModel):
    key: str

    value: str


class DataAPIKeyConfiguration(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[DataAPIKeyConfigurationValue]] = None


class DataAPIKeyPermission(BaseModel):
    name: str


class DataAPIKeyUserRolePermission(BaseModel):
    name: str


class DataAPIKeyUserRole(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[DataAPIKeyUserRolePermission]] = None


class DataAPIKeyUser(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[DataAPIKeyUserRole]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None


class DataAPIKey(BaseModel):
    id: str

    prefix: str

    status: Literal["active", "revoked"]

    configurations: Optional[List[DataAPIKeyConfiguration]] = None

    created_at: Optional[datetime] = None

    permissions: Optional[List[DataAPIKeyPermission]] = None

    revoked_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    user: Optional[DataAPIKeyUser] = None


class Data(BaseModel):
    api_key: Optional[DataAPIKey] = None

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
