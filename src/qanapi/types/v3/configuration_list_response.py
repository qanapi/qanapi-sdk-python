# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ConfigurationListResponse", "ConfigurationListResponseItem", "ConfigurationListResponseItemValue"]


class ConfigurationListResponseItemValue(BaseModel):
    key: str

    value: str


class ConfigurationListResponseItem(BaseModel):
    id: str

    name: str

    type: str

    values: Optional[List[ConfigurationListResponseItemValue]] = None


ConfigurationListResponse: TypeAlias = List[ConfigurationListResponseItem]
