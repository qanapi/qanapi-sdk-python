# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Decrypt"]


class Decrypt(BaseModel):
    data: Union[str, Dict[str, object], List[object]]
    """The encrypted payload to decrypt.

    - Can be a string or an object/array with encrypted fields.
    - Decryption is selective if `sensitiveFields` is provided.
    """

    sensitive_fields: Optional[List[str]] = FieldInfo(alias="sensitiveFields", default=None)
    """Laravel-style dot-notated paths to fields to decrypt.

    - Same syntax and behavior as in EncryptRequest.
    - If omitted, all string values matching encryption prefix are attempted.

    Examples:

    - `user.ssn`
    - `employees.*.payroll.token`
    """
