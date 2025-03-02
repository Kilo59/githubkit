"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0087 import RepositoryRulesetConditionsPropRefNameType
from .group_0089 import (
    RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType,
)
from .group_0091 import (
    EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationIdType,
)


class EnterpriseRulesetConditionsOneof3Type(TypedDict):
    """organization_id_and_repository_property

    Conditions to target organization by id and repositories by property
    """

    organization_id: (
        EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationIdType
    )
    repository_property: (
        RepositoryRulesetConditionsRepositoryPropertyTargetPropRepositoryPropertyType
    )
    ref_name: NotRequired[RepositoryRulesetConditionsPropRefNameType]


__all__ = ("EnterpriseRulesetConditionsOneof3Type",)
