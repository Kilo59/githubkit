"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0068 import RepositoryRulesetBypassActorType
from .group_0073 import RepositoryRulesetConditionsType
from .group_0083 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0084 import RepositoryRuleUpdateType
from .group_0086 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0087 import RepositoryRuleMergeQueueType
from .group_0089 import RepositoryRuleRequiredDeploymentsType
from .group_0092 import RepositoryRulePullRequestType
from .group_0094 import RepositoryRuleRequiredStatusChecksType
from .group_0096 import RepositoryRuleCommitMessagePatternType
from .group_0098 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0100 import RepositoryRuleCommitterEmailPatternType
from .group_0102 import RepositoryRuleBranchNamePatternType
from .group_0104 import RepositoryRuleTagNamePatternType
from .group_0107 import RepositoryRuleWorkflowsType
from .group_0109 import RepositoryRuleCodeScanningType
from .group_0111 import RepositoryRuleOneof18Type
from .group_0114 import OrgRulesetConditionsOneof0Type
from .group_0115 import OrgRulesetConditionsOneof1Type
from .group_0116 import OrgRulesetConditionsOneof2Type


class RepositoryRulesetType(TypedDict):
    """Repository ruleset

    A set of rules to apply when specified conditions are met.
    """

    id: int
    name: str
    target: NotRequired[Literal["branch", "tag", "push", "repository"]]
    source_type: NotRequired[Literal["Repository", "Organization", "Enterprise"]]
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
    "RepositoryRulesetPropLinksPropHtmlType",
    "RepositoryRulesetPropLinksPropSelfType",
    "RepositoryRulesetPropLinksType",
    "RepositoryRulesetType",
)
