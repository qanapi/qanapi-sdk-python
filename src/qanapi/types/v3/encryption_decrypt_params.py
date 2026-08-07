# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EncryptionDecryptParams"]


class EncryptionDecryptParams(TypedDict, total=False):
    data: Required[Dict[str, object]]
    """A JSON object to decrypt fields on. A maximum depth of 32 is allowed."""

    x_qanapi_fields: Required[Annotated[str, PropertyInfo(alias="x-qanapi-fields")]]
