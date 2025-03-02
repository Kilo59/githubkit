"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBody(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBody"""

    dismissal_restrictions: Missing[
        ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDismissalRestrictions
    ] = Field(
        default=UNSET,
        description="Specify which users, teams, and apps can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories.",
    )
    dismiss_stale_reviews: Missing[bool] = Field(
        default=UNSET,
        description="Set to `true` if you want to automatically dismiss approving reviews when someone pushes a new commit.",
    )
    require_code_owner_reviews: Missing[bool] = Field(
        default=UNSET,
        description="Blocks merging pull requests until [code owners](https://docs.github.com/enterprise-cloud@latest//articles/about-code-owners/) have reviewed.",
    )
    required_approving_review_count: Missing[int] = Field(
        default=UNSET,
        description="Specifies the number of reviewers required to approve pull requests. Use a number between 1 and 6 or 0 to not require reviewers.",
    )
    require_last_push_approval: Missing[bool] = Field(
        default=UNSET,
        description="Whether the most recent push must be approved by someone other than the person who pushed it. Default: `false`",
    )
    bypass_pull_request_allowances: Missing[
        ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropBypassPullRequestAllowances
    ] = Field(
        default=UNSET,
        description="Allow specific users, teams, or apps to bypass pull request requirements.",
    )


class ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDismissalRestrictions(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDis
    missalRestrictions

    Specify which users, teams, and apps can dismiss pull request reviews. Pass an
    empty `dismissal_restrictions` object to disable. User and team
    `dismissal_restrictions` are only available for organization-owned repositories.
    Omit this parameter for personal repositories.
    """

    users: Missing[list[str]] = Field(
        default=UNSET, description="The list of user `login`s with dismissal access"
    )
    teams: Missing[list[str]] = Field(
        default=UNSET, description="The list of team `slug`s with dismissal access"
    )
    apps: Missing[list[str]] = Field(
        default=UNSET, description="The list of app `slug`s with dismissal access"
    )


class ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropBypassPullRequestAllowances(
    GitHubModel
):
    """ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropByp
    assPullRequestAllowances

    Allow specific users, teams, or apps to bypass pull request requirements.
    """

    users: Missing[list[str]] = Field(
        default=UNSET,
        description="The list of user `login`s allowed to bypass pull request requirements.",
    )
    teams: Missing[list[str]] = Field(
        default=UNSET,
        description="The list of team `slug`s allowed to bypass pull request requirements.",
    )
    apps: Missing[list[str]] = Field(
        default=UNSET,
        description="The list of app `slug`s allowed to bypass pull request requirements.",
    )


model_rebuild(ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBody)
model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDismissalRestrictions
)
model_rebuild(
    ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropBypassPullRequestAllowances
)

__all__ = (
    "ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBody",
    "ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropBypassPullRequestAllowances",
    "ReposOwnerRepoBranchesBranchProtectionRequiredPullRequestReviewsPatchBodyPropDismissalRestrictions",
)
