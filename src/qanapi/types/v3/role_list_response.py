# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["RoleListResponse", "RoleListResponseItem", "RoleListResponseItemPermission"]


class RoleListResponseItemPermission(BaseModel):
    name: str


class RoleListResponseItem(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[RoleListResponseItemPermission]] = None


RoleListResponse: TypeAlias = List[RoleListResponseItem]
