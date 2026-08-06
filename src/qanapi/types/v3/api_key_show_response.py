# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "APIKeyShowResponse",
    "Configuration",
    "ConfigurationValue",
    "Permission",
    "User",
    "UserRole",
    "UserRolePermission",
]


class ConfigurationValue(BaseModel):
    key: str

    value: str


class Configuration(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[ConfigurationValue]] = None


class Permission(BaseModel):
    name: str


class UserRolePermission(BaseModel):
    name: str


class UserRole(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[UserRolePermission]] = None


class User(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[UserRole]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None


class APIKeyShowResponse(BaseModel):
    id: str

    prefix: str

    status: Literal["active", "revoked"]

    configurations: Optional[List[Configuration]] = None

    created_at: Optional[datetime] = None

    permissions: Optional[List[Permission]] = None

    revoked_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    user: Optional[User] = None
