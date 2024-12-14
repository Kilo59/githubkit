"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict

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
