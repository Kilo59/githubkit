"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing_extensions import TypedDict


class ActionsVariableType(TypedDict):
    """Actions Variable"""

    name: str
    value: str
    created_at: datetime
    updated_at: datetime


__all__ = ("ActionsVariableType",)
