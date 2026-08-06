# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..user import User
from ..api_key import APIKey
from ..._models import BaseModel
from ..configuration import Configuration

__all__ = [
    "LogUnifiedResponse",
    "Data",
    "DataFullLog",
    "DataFullLogActivityLog",
    "DataFullLogAPILog",
    "DataFullLogQanapiFlowLog",
    "Link",
]


class DataFullLogActivityLog(BaseModel):
    action: Optional[str] = None

    description: Optional[str] = None

    ip: Optional[str] = None

    timestamp: Optional[datetime] = None

    user: Optional[User] = None

    when: Optional[str] = None


class DataFullLogAPILog(BaseModel):
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


class DataFullLogQanapiFlowLog(BaseModel):
    action: Optional[str] = None

    configuration_id: Optional[int] = None

    created_at: Optional[datetime] = None

    email: Optional[str] = None

    request_id: Optional[str] = None

    type: Optional[str] = None


DataFullLog: TypeAlias = Union[DataFullLogActivityLog, DataFullLogAPILog, DataFullLogQanapiFlowLog]


class Data(BaseModel):
    action: Optional[str] = None

    causer_email: Optional[str] = None

    configuration: Optional[Configuration] = None

    description: Optional[str] = None

    details: Optional[object] = None

    full_log: Optional[DataFullLog] = None

    log_type: Optional[Literal["activity", "api", "usage"]] = None

    request_id: Optional[str] = None

    status_code: Optional[int] = None

    timestamp: Optional[datetime] = None

    user: Optional[User] = None


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
