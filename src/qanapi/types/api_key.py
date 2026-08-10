# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .user import User
from .._models import BaseModel
from .permission import Permission
from .configuration import Configuration

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str

    prefix: str

    status: Literal["active", "revoked"]

    configurations: Optional[List[Configuration]] = None

    created_at: Optional[datetime] = None

    permissions: Optional[List[Permission]] = None

    revoked_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None

    user: Optional[User] = None
