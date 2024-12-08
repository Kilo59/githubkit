"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0111 import RepositoryRulesetBypassActor
from .group_0112 import RepositoryRulesetConditions
from .group_0123 import (
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleRequiredSignatures,
)
from .group_0124 import RepositoryRuleUpdate
from .group_0126 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0127 import RepositoryRuleMergeQueue
from .group_0129 import RepositoryRuleRequiredDeployments
from .group_0132 import RepositoryRulePullRequest
from .group_0134 import RepositoryRuleRequiredStatusChecks
from .group_0136 import RepositoryRuleCommitMessagePattern
from .group_0138 import RepositoryRuleCommitAuthorEmailPattern
from .group_0140 import RepositoryRuleCommitterEmailPattern
from .group_0142 import RepositoryRuleBranchNamePattern
from .group_0144 import RepositoryRuleTagNamePattern
from .group_0147 import RepositoryRuleWorkflows
from .group_0149 import RepositoryRuleCodeScanning
from .group_0151 import RepositoryRuleOneof18


class ReposOwnerRepoRulesetsRulesetIdPutBody(GitHubModel):
    """ReposOwnerRepoRulesetsRulesetIdPutBody"""

    name: Missing[str] = Field(default=UNSET, description="The name of the ruleset.")
    target: Missing[Literal["branch", "tag", "push"]] = Field(
        default=UNSET, description="The target of the ruleset"
    )
    enforcement: Missing[Literal["disabled", "active", "evaluate"]] = Field(
        default=UNSET,
        description="The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise).",
    )
    bypass_actors: Missing[list[RepositoryRulesetBypassActor]] = Field(
        default=UNSET,
        description="The actors that can bypass the rules in this ruleset",
    )
    conditions: Missing[RepositoryRulesetConditions] = Field(
        default=UNSET,
        title="Repository ruleset conditions for ref names",
        description="Parameters for a repository ruleset ref name condition",
    )
    rules: Missing[
        list[
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
        ]
    ] = Field(default=UNSET, description="An array of rules within the ruleset.")


model_rebuild(ReposOwnerRepoRulesetsRulesetIdPutBody)

__all__ = ("ReposOwnerRepoRulesetsRulesetIdPutBody",)
