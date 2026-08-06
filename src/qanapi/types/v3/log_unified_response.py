# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "LogUnifiedResponse",
    "Data",
    "DataConfiguration",
    "DataConfigurationValue",
    "DataFullLog",
    "DataFullLogActivityLog",
    "DataFullLogActivityLogUser",
    "DataFullLogActivityLogUserRole",
    "DataFullLogActivityLogUserRolePermission",
    "DataFullLogAPILog",
    "DataFullLogAPILogAPIKey",
    "DataFullLogAPILogAPIKeyConfiguration",
    "DataFullLogAPILogAPIKeyConfigurationValue",
    "DataFullLogAPILogAPIKeyPermission",
    "DataFullLogAPILogAPIKeyUser",
    "DataFullLogAPILogAPIKeyUserRole",
    "DataFullLogAPILogAPIKeyUserRolePermission",
    "DataFullLogQanapiFlowLog",
    "DataUser",
    "DataUserRole",
    "DataUserRolePermission",
    "Link",
]


class DataConfigurationValue(BaseModel):
    key: str

    value: str


class DataConfiguration(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[DataConfigurationValue]] = None


class DataFullLogActivityLogUserRolePermission(BaseModel):
    name: str


class DataFullLogActivityLogUserRole(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[DataFullLogActivityLogUserRolePermission]] = None


class DataFullLogActivityLogUser(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[DataFullLogActivityLogUserRole]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None


class DataFullLogActivityLog(BaseModel):
    action: Optional[str] = None

    description: Optional[str] = None

    ip: Optional[str] = None

    timestamp: Optional[datetime] = None

    user: Optional[DataFullLogActivityLogUser] = None

    when: Optional[str] = None


class DataFullLogAPILogAPIKeyConfigurationValue(BaseModel):
    key: str

    value: str


class DataFullLogAPILogAPIKeyConfiguration(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[DataFullLogAPILogAPIKeyConfigurationValue]] = None


class DataFullLogAPILogAPIKeyPermission(BaseModel):
    name: str


class DataFullLogAPILogAPIKeyUserRolePermission(BaseModel):
    name: str


class DataFullLogAPILogAPIKeyUserRole(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[DataFullLogAPILogAPIKeyUserRolePermission]] = None


class DataFullLogAPILogAPIKeyUser(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[DataFullLogAPILogAPIKeyUserRole]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None


class DataFullLogAPILogAPIKey(BaseModel):
    id: str

    prefix: str

    status: Literal["active", "revoked"]

    configurations: Optional[List[DataFullLogAPILogAPIKeyConfiguration]] = None

    created_at: Optional[datetime] = None

    permissions: Optional[List[DataFullLogAPILogAPIKeyPermission]] = None

    revoked_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    user: Optional[DataFullLogAPILogAPIKeyUser] = None


class DataFullLogAPILog(BaseModel):
    api_key: Optional[DataFullLogAPILogAPIKey] = None

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


class DataFullLogQanapiFlowLog(BaseModel):
    action: Optional[str] = None

    configuration_id: Optional[int] = None

    created_at: Optional[datetime] = None

    email: Optional[str] = None

    request_id: Optional[str] = None

    type: Optional[str] = None


DataFullLog: TypeAlias = Union[DataFullLogActivityLog, DataFullLogAPILog, DataFullLogQanapiFlowLog]


class DataUserRolePermission(BaseModel):
    name: str


class DataUserRole(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[DataUserRolePermission]] = None


class DataUser(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[DataUserRole]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None


class Data(BaseModel):
    action: Optional[str] = None

    causer_email: Optional[str] = None

    configuration: Optional[DataConfiguration] = None

    description: Optional[str] = None

    details: Optional[object] = None

    full_log: Optional[DataFullLog] = None

    log_type: Optional[Literal["activity", "api", "usage"]] = None

    request_id: Optional[str] = None

    status_code: Optional[int] = None

    timestamp: Optional[datetime] = None

    user: Optional[DataUser] = None


class Link(BaseModel):
    active: Optional[bool] = None

    label: Optional[str] = None

    page: Optional[int] = None

    url: Optional[str] = None


class LogUnifiedResponse(BaseModel):
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
