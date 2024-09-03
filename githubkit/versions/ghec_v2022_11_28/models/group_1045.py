"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0280 import CustomDeploymentRuleApp


class ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesAppsGetResponse200(
    GitHubModel
):
    """ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesAppsGetRespons
    e200
    """

    total_count: Missing[int] = Field(
        default=UNSET,
        description="The total number of custom deployment protection rule integrations available for this environment.",
    )
    available_custom_deployment_protection_rule_integrations: Missing[
        List[CustomDeploymentRuleApp]
    ] = Field(default=UNSET)


model_rebuild(
    ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesAppsGetResponse200
)

__all__ = (
    "ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentProtectionRulesAppsGetResponse200",
)
