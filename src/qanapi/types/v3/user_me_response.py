# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UserMeResponse", "Role", "RolePermission"]


class RolePermission(BaseModel):
    name: str


class Role(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[RolePermission]] = None


class UserMeResponse(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[Role]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None
