# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["UserListResponse", "UserListResponseItem", "UserListResponseItemRole", "UserListResponseItemRolePermission"]


class UserListResponseItemRolePermission(BaseModel):
    name: str


class UserListResponseItemRole(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[UserListResponseItemRolePermission]] = None


class UserListResponseItem(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[UserListResponseItemRole]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None


UserListResponse: TypeAlias = List[UserListResponseItem]
