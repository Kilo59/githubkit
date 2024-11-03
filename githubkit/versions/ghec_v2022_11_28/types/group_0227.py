"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0050 import TeamType
from .group_0002 import SimpleUserType
from .group_0008 import IntegrationType


class ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictionsType(
    TypedDict
):
    """ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictions"""

    url: str
    users_url: str
    teams_url: str
    users: list[SimpleUserType]
    teams: list[TeamType]
    apps: NotRequired[list[Union[IntegrationType, None]]]


class ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowancesType(
    TypedDict
):
    """ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowances"""

    users: list[SimpleUserType]
    teams: list[TeamType]
    apps: NotRequired[list[Union[IntegrationType, None]]]


__all__ = (
    "ProtectedBranchPropRequiredPullRequestReviewsPropDismissalRestrictionsType",
    "ProtectedBranchPropRequiredPullRequestReviewsPropBypassPullRequestAllowancesType",
)
