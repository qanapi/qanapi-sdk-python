# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Encrypt", "Access", "Attributes"]


class Access(BaseModel):
    acl: Optional[List[str]] = None
    """Access control list — list of user roles authorized to decrypt this data."""


class Attributes(BaseModel):
    classification: Optional[Literal["public", "internal", "confidential", "restricted"]] = None

    owner: Optional[str] = None

    tags: Optional[List[str]] = None


class Encrypt(BaseModel):
    data: Union[str, float, Dict[str, object], List[object]]
    """The actual data to encrypt.

    - Can be a scalar (string/number), object, or array.
    - If the value is an object or array, only the specified `sensitiveFields` are
      encrypted.
    """

    access: Optional[Access] = None

    attributes: Optional[Attributes] = None
    """Optional metadata describing the data's context."""

    sensitive_fields: Optional[List[str]] = FieldInfo(alias="sensitiveFields", default=None)
    """Laravel-style dot-notated paths to fields that should be encrypted.

    Supports:

    - Dot notation for nested fields: `user.profile.ssn`
    - Wildcard `*` for arrays or dynamic keys: `users.*.token`

    Examples:

    - `password`
    - `user.credentials.secret`
    - `accounts.*.secret`
    - `teams.*.members.*.email`
    """
