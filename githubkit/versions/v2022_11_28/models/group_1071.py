"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0122 import RepositoryRuleUpdate
from .group_0149 import RepositoryRuleOneof18
from .group_0145 import RepositoryRuleWorkflows
from .group_0125 import RepositoryRuleMergeQueue
from .group_0130 import RepositoryRulePullRequest
from .group_0147 import RepositoryRuleCodeScanning
from .group_0110 import RepositoryRulesetConditions
from .group_0109 import RepositoryRulesetBypassActor
from .group_0142 import RepositoryRuleTagNamePattern
from .group_0140 import RepositoryRuleBranchNamePattern
from .group_0127 import RepositoryRuleRequiredDeployments
from .group_0132 import RepositoryRuleRequiredStatusChecks
from .group_0134 import RepositoryRuleCommitMessagePattern
from .group_0138 import RepositoryRuleCommitterEmailPattern
from .group_0136 import RepositoryRuleCommitAuthorEmailPattern
from .group_0124 import RepositoryRuleOneof16, RepositoryRuleRequiredLinearHistory
from .group_0121 import (
    RepositoryRuleOneof15,
    RepositoryRuleOneof17,
    RepositoryRuleCreation,
    RepositoryRuleDeletion,
    RepositoryRuleNonFastForward,
    RepositoryRuleRequiredSignatures,
)


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
