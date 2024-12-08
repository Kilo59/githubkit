"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0155 import RepositoryRuleUpdatePropParametersType


class RepositoryRuleUpdateType(TypedDict):
    """update

    Only allow users with bypass permission to update matching refs.
    """

    type: Literal["update"]
    parameters: NotRequired[RepositoryRuleUpdatePropParametersType]


__all__ = ("RepositoryRuleUpdateType",)
