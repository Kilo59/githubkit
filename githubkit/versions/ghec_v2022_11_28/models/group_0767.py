"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0153 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleRequiredSignatures,
)
from .group_0154 import RepositoryRuleUpdate
from .group_0156 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0157 import RepositoryRuleMergeQueue
from .group_0159 import RepositoryRuleRequiredDeployments
from .group_0162 import RepositoryRulePullRequest
from .group_0164 import RepositoryRuleRequiredStatusChecks
from .group_0166 import RepositoryRuleCommitMessagePattern
from .group_0168 import RepositoryRuleCommitAuthorEmailPattern
from .group_0170 import RepositoryRuleCommitterEmailPattern
from .group_0172 import RepositoryRuleBranchNamePattern
from .group_0174 import RepositoryRuleTagNamePattern
from .group_0177 import RepositoryRuleWorkflows
from .group_0179 import RepositoryRuleCodeScanning
from .group_0181 import RepositoryRuleOneof18


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems"""

    rule: Missing[
        Union[
            RepositoryRuleCreation,
            RepositoryRuleUpdate,
            RepositoryRuleDeletion,
            RepositoryRuleRequiredLinearHistory,
            RepositoryRuleMergeQueue,
            RepositoryRuleRequiredDeployments,
            RepositoryRuleRequiredSignatures,
            RepositoryRulePullRequest,
            RepositoryRuleRequiredStatusChecks,
            RepositoryRuleNonFastForward,
            RepositoryRuleCommitMessagePattern,
            RepositoryRuleCommitAuthorEmailPattern,
            RepositoryRuleCommitterEmailPattern,
            RepositoryRuleBranchNamePattern,
            RepositoryRuleTagNamePattern,
            RepositoryRuleOneof15,
            RepositoryRuleOneof16,
            RepositoryRuleOneof17,
            RepositoryRuleOneof18,
            RepositoryRuleWorkflows,
            RepositoryRuleCodeScanning,
        ]
    ] = Field(default=UNSET, title="Repository Rule", description="A repository rule.")
    changes: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges"""

    configuration: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration
    ] = Field(default=UNSET)
    rule_type: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType
    ] = Field(default=UNSET)
    pattern: Missing[
        WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern
    ] = Field(default=UNSET)


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pConfiguration
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pRuleType
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


class WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern(
    GitHubModel
):
    """WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPro
    pPattern
    """

    from_: Missing[str] = Field(default=UNSET, alias="from")


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType
)
model_rebuild(
    WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern
)

__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItems",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChanges",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropConfiguration",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropPattern",
    "WebhookRepositoryRulesetEditedPropChangesPropRulesPropUpdatedItemsPropChangesPropRuleType",
)
