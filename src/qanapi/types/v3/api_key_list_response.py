# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "APIKeyListResponse",
    "APIKeyListResponseItem",
    "APIKeyListResponseItemConfiguration",
    "APIKeyListResponseItemConfigurationValue",
    "APIKeyListResponseItemPermission",
    "APIKeyListResponseItemUser",
    "APIKeyListResponseItemUserRole",
    "APIKeyListResponseItemUserRolePermission",
]


class APIKeyListResponseItemConfigurationValue(BaseModel):
    key: str

    value: str


class APIKeyListResponseItemConfiguration(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[APIKeyListResponseItemConfigurationValue]] = None


class APIKeyListResponseItemPermission(BaseModel):
    name: str


class APIKeyListResponseItemUserRolePermission(BaseModel):
    name: str


class APIKeyListResponseItemUserRole(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[APIKeyListResponseItemUserRolePermission]] = None


class APIKeyListResponseItemUser(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[APIKeyListResponseItemUserRole]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None


class APIKeyListResponseItem(BaseModel):
    id: str

    prefix: str

    status: Literal["active", "revoked"]

    configurations: Optional[List[APIKeyListResponseItemConfiguration]] = None

    created_at: Optional[datetime] = None

    permissions: Optional[List[APIKeyListResponseItemPermission]] = None

    revoked_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    user: Optional[APIKeyListResponseItemUser] = None


APIKeyListResponse: TypeAlias = List[APIKeyListResponseItem]
