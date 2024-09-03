"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0381 import WebhooksRuleType
from .group_0376 import EnterpriseWebhooksType
from .group_0377 import SimpleInstallationType
from .group_0379 import RepositoryWebhooksType
from .group_0380 import SimpleUserWebhooksType
from .group_0378 import OrganizationSimpleWebhooksType


class WebhookBranchProtectionRuleEditedType(TypedDict):
    """branch protection rule edited event"""

    action: Literal["edited"]
    changes: NotRequired[WebhookBranchProtectionRuleEditedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    rule: WebhooksRuleType
    sender: SimpleUserWebhooksType


class WebhookBranchProtectionRuleEditedPropChangesType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChanges

    If the action was `edited`, the changes to the rule.
    """

    admin_enforced: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType
    ]
    authorized_actor_names: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType
    ]
    authorized_actors_only: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType
    ]
    authorized_dismissal_actors_only: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType
    ]
    linear_history_requirement_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType
    ]
    lock_branch_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevelType
    ]
    lock_allows_fork_sync: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSyncType
    ]
    pull_request_reviews_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevelType
    ]
    require_last_push_approval: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApprovalType
    ]
    required_status_checks: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType
    ]
    required_status_checks_enforcement_level: NotRequired[
        WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType
    ]


class WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforced"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNames"""

    from_: List[str]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnly"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnly"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcem
    entLevel
    """

    from_: Literal["off", "non_admins", "everyone"]


class WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevel"""

    from_: Literal["off", "non_admins", "everyone"]


class WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSyncType(TypedDict):
    """WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSync"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLev
    el
    """

    from_: Literal["off", "non_admins", "everyone"]


class WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApprovalType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApproval"""

    from_: Union[bool, None]


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecks"""

    from_: List[str]


class WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType(
    TypedDict
):
    """WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementL
    evel
    """

    from_: Literal["off", "non_admins", "everyone"]


__all__ = (
    "WebhookBranchProtectionRuleEditedType",
    "WebhookBranchProtectionRuleEditedPropChangesType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAdminEnforcedType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorNamesType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedActorsOnlyType",
    "WebhookBranchProtectionRuleEditedPropChangesPropAuthorizedDismissalActorsOnlyType",
    "WebhookBranchProtectionRuleEditedPropChangesPropLinearHistoryRequirementEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropLockBranchEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropLockAllowsForkSyncType",
    "WebhookBranchProtectionRuleEditedPropChangesPropPullRequestReviewsEnforcementLevelType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequireLastPushApprovalType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksType",
    "WebhookBranchProtectionRuleEditedPropChangesPropRequiredStatusChecksEnforcementLevelType",
)
