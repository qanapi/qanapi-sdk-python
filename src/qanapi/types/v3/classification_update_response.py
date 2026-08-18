# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..role import Role
from ..user import User
from ..._models import BaseModel
from ..google_group import GoogleGroup

__all__ = ["ClassificationUpdateResponse", "Provider"]


class Provider(BaseModel):
    gws_groups: Optional[List[GoogleGroup]] = None

    name: Optional[str] = None

    uuid: Optional[str] = None


class ClassificationUpdateResponse(BaseModel):
    id: int

    bg_color: str

    fg_color: str

    name: str

    slug: str

    description: Optional[str] = None

    emoji: Optional[str] = None

    providers: Optional[List[Provider]] = None

    roles: Optional[List[Role]] = None

    users: Optional[List[User]] = None
