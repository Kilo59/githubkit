"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0124 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleOneof15Type,
    RepositoryRuleOneof17Type,
    RepositoryRuleRequiredSignaturesType,
)
from .group_0125 import RepositoryRuleUpdateType
from .group_0127 import (
    RepositoryRuleOneof16Type,
    RepositoryRuleRequiredLinearHistoryType,
)
from .group_0128 import RepositoryRuleMergeQueueType
from .group_0130 import RepositoryRuleRequiredDeploymentsType
from .group_0133 import RepositoryRulePullRequestType
from .group_0135 import RepositoryRuleRequiredStatusChecksType
from .group_0137 import RepositoryRuleCommitMessagePatternType
from .group_0139 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0141 import RepositoryRuleCommitterEmailPatternType
from .group_0143 import RepositoryRuleBranchNamePatternType
from .group_0145 import RepositoryRuleTagNamePatternType
from .group_0148 import RepositoryRuleWorkflowsType
from .group_0150 import RepositoryRuleCodeScanningType
from .group_0152 import RepositoryRuleOneof18Type


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType(TypedDict):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems"""

    rule: NotRequired[
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
    changes: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesType
    ]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges"""

    configuration: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfigurationType
    ]
    rule_type: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleTypeType
    ]
    pattern: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPatternType
    ]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfigurationType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pConfiguration
    """

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleTypeType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pRuleType
    """

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPatternType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pPattern
    """

    from_: NotRequired[str]


__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfigurationType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPatternType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleTypeType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesType",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsType",
)
