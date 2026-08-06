# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ConfigurationUpdateResponse", "Value"]


class Value(BaseModel):
    key: str

    value: str


class ConfigurationUpdateResponse(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[Value]] = None
