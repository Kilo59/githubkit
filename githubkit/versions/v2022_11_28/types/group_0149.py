"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0122 import RepositoryRuleUpdateType
from .group_0148 import RepositoryRuleOneof18Type
from .group_0144 import RepositoryRuleWorkflowsType
from .group_0125 import RepositoryRuleMergeQueueType
from .group_0129 import RepositoryRulePullRequestType
from .group_0118 import OrgRulesetConditionsOneof0Type
from .group_0119 import OrgRulesetConditionsOneof1Type
from .group_0120 import OrgRulesetConditionsOneof2Type
from .group_0146 import RepositoryRuleCodeScanningType
from .group_0110 import RepositoryRulesetConditionsType
from .group_0109 import RepositoryRulesetBypassActorType
from .group_0141 import RepositoryRuleTagNamePatternType
from .group_0139 import RepositoryRuleBranchNamePatternType
from .group_0127 import RepositoryRuleRequiredDeploymentsType
from .group_0131 import RepositoryRuleRequiredStatusChecksType
from .group_0133 import RepositoryRuleCommitMessagePatternType
from .group_0137 import RepositoryRuleCommitterEmailPatternType
from .group_0135 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0124 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0121 import (
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class RepositoryRulesetType(TypedDict):
    """Repository ruleset

    A set of rules to apply when specified conditions are met.
    """

    id: int
    name: str
    target: NotRequired[Literal["branch", "tag", "push"]]
    source_type: NotRequired[Literal["Repository", "Organization"]]
    source: str
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: NotRequired[list[RepositoryRulesetBypassActorType]]
    current_user_can_bypass: NotRequired[
        Literal["always", "pull_requests_only", "never"]
    ]
    node_id: NotRequired[str]
    links: NotRequired[RepositoryRulesetPropLinksType]
    conditions: NotRequired[
        Union[
            RepositoryRulesetConditionsType,
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            OrgRulesetConditionsOneof2Type,
            None,
        ]
    ]
    rules: NotRequired[
        list[
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
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


class RepositoryRulesetPropLinksType(TypedDict):
    """RepositoryRulesetPropLinks"""

    self_: NotRequired[RepositoryRulesetPropLinksPropSelfType]
    html: NotRequired[Union[RepositoryRulesetPropLinksPropHtmlType, None]]


class RepositoryRulesetPropLinksPropSelfType(TypedDict):
    """RepositoryRulesetPropLinksPropSelf"""

    href: NotRequired[str]


class RepositoryRulesetPropLinksPropHtmlType(TypedDict):
    """RepositoryRulesetPropLinksPropHtml"""

    href: NotRequired[str]


__all__ = (
    "RepositoryRulesetType",
    "RepositoryRulesetPropLinksType",
    "RepositoryRulesetPropLinksPropSelfType",
    "RepositoryRulesetPropLinksPropHtmlType",
)
