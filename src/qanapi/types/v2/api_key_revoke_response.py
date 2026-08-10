# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["APIKeyRevokeResponse"]


class APIKeyRevokeResponse(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    revoked_at: Optional[datetime] = None
