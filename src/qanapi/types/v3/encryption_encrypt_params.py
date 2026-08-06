# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EncryptionEncryptParams"]


class EncryptionEncryptParams(TypedDict, total=False):
    body: Required[Dict[str, object]]
    """A JSON object to encrypt fields on. A maximum depth of 32 is allowed."""

    x_qanapi_fields: Required[Annotated[str, PropertyInfo(alias="x-qanapi-fields")]]

    x_qanapi_destination: Annotated[str, PropertyInfo(alias="x-qanapi-destination")]
