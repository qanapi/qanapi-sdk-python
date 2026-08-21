# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..role import Role
from ..user import User
from ..._models import BaseModel
from ..google_group import GoogleGroup

__all__ = ["ClassificationListResponse", "Data", "DataProvider", "Link"]


class DataProvider(BaseModel):
    gws_groups: Optional[List[GoogleGroup]] = None

    name: Optional[str] = None

    uuid: Optional[str] = None


class Data(BaseModel):
    id: int

    bg_color: str

    fg_color: str

    name: str

    slug: str

    description: Optional[str] = None

    emoji: Optional[str] = None

    providers: Optional[List[DataProvider]] = None

    roles: Optional[List[Role]] = None

    users: Optional[List[User]] = None


class Link(BaseModel):
    active: Optional[bool] = None

    label: Optional[str] = None

    page: Optional[int] = None

    url: Optional[str] = None


class ClassificationListResponse(BaseModel):
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
