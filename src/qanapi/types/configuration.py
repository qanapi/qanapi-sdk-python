# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .value import Value
from .._models import BaseModel

__all__ = ["Configuration"]


class Configuration(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[Value]] = None
