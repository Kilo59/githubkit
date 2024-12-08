"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0113 import RepositoryRulesetConditionsPropRefNameType
from .group_0115 import (
    RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType,
)


class OrgRulesetConditionsOneof0Type(TypedDict):
    """repository_name_and_ref_name

    Conditions to target repositories by name and refs by name
    """

    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]
    repository_name: (
        RepositoryRulesetConditionsRepositoryNameTargetPropRepositoryNameType
    )


__all__ = ("OrgRulesetConditionsOneof0Type",)
