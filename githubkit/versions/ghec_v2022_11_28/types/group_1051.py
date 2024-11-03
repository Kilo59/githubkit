"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentBranchPoliciesGetResponse200Type(
    TypedDict
):
    """ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentBranchPoliciesGetResponse200"""

    total_count: int
    branch_policies: list[DeploymentBranchPolicyType]


class DeploymentBranchPolicyType(TypedDict):
    """Deployment branch policy

    Details of a deployment branch or tag policy.
    """

    id: NotRequired[int]
    node_id: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[Literal["branch", "tag"]]


__all__ = (
    "ReposOwnerRepoEnvironmentsEnvironmentNameDeploymentBranchPoliciesGetResponse200Type",
    "DeploymentBranchPolicyType",
)
