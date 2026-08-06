# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .permission import Permission

__all__ = ["Role"]


class Role(BaseModel):
    name: str

    description: Optional[str] = None

    permissions: Optional[List[Permission]] = None
