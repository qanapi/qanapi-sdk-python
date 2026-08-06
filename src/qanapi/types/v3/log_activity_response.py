# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LogActivityResponse", "Data", "DataUser", "DataUserRole", "DataUserRolePermission", "Link"]


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

    description: Optional[str] = None

    ip: Optional[str] = None

    timestamp: Optional[datetime] = None

    user: Optional[DataUser] = None

    when: Optional[str] = None


class Link(BaseModel):
    active: Optional[bool] = None

    label: Optional[str] = None

    page: Optional[int] = None

    url: Optional[str] = None


class LogActivityResponse(BaseModel):
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
