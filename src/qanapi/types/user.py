# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .role import Role
from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: int

    email: str

    name: str

    created_at: Optional[datetime] = None

    roles: Optional[List[Role]] = None

    two_factor_enabled: Optional[bool] = None

    updated_at: Optional[datetime] = None
