"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0074 import RepositoryRulesetConditionsPropRefNameType
from .group_0113 import (
    RepositoryRulesetConditionsRepositoryIdTargetPropRepositoryIdType,
)


class OrgRulesetConditionsOneof1Type(TypedDict):
    """repository_id_and_ref_name

    Conditions to target repositories by id and refs by name
    """

    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]
    repository_id: RepositoryRulesetConditionsRepositoryIdTargetPropRepositoryIdType


__all__ = ("OrgRulesetConditionsOneof1Type",)
