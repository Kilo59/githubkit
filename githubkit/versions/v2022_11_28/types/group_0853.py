"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0114 import RepositoryRuleUpdateType
from .group_0140 import RepositoryRuleOneof18Type
from .group_0136 import RepositoryRuleWorkflowsType
from .group_0117 import RepositoryRuleMergeQueueType
from .group_0121 import RepositoryRulePullRequestType
from .group_0110 import OrgRulesetConditionsOneof0Type
from .group_0111 import OrgRulesetConditionsOneof1Type
from .group_0112 import OrgRulesetConditionsOneof2Type
from .group_0138 import RepositoryRuleCodeScanningType
from .group_0101 import RepositoryRulesetBypassActorType
from .group_0133 import RepositoryRuleTagNamePatternType
from .group_0131 import RepositoryRuleBranchNamePatternType
from .group_0119 import RepositoryRuleRequiredDeploymentsType
from .group_0123 import RepositoryRuleRequiredStatusChecksType
from .group_0125 import RepositoryRuleCommitMessagePatternType
from .group_0129 import RepositoryRuleCommitterEmailPatternType
from .group_0127 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0116 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0113 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class OrgsOrgRulesetsPostBodyType(TypedDict):
    """OrgsOrgRulesetsPostBody"""

    name: str
    target: NotRequired[Literal["branch", "tag", "push"]]
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: NotRequired[List[RepositoryRulesetBypassActorType]]
    conditions: NotRequired[
        Union[
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            OrgRulesetConditionsOneof2Type,
        ]
    ]
    rules: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleMergeQueueType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleOneof15Type,
                RepositoryRuleOneof16Type,
                RepositoryRuleOneof17Type,
                RepositoryRuleOneof18Type,
                RepositoryRuleWorkflowsType,
                RepositoryRuleCodeScanningType,
            ]
        ]
    ]


__all__ = ("OrgsOrgRulesetsPostBodyType",)
