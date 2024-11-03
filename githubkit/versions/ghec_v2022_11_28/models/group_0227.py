"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0050 import Team
from .group_0002 import SimpleUser
from .group_0008 import Integration


class ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions(
    GitHubModel
):
    """ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions"""

    url: str = Field()
    users_url: str = Field()
    teams_url: str = Field()
    users: list[SimpleUser] = Field()
    teams: list[Team] = Field()
    apps: Missing[list[Union[Integration, None]]] = Field(default=UNSET)


class ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances(
    GitHubModel
):
    """ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances"""

    users: list[SimpleUser] = Field()
    teams: list[Team] = Field()
    apps: Missing[list[Union[Integration, None]]] = Field(default=UNSET)


model_rebuild(ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions)
model_rebuild(
    ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances
)

__all__ = (
    "ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions",
    "ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances",
)
