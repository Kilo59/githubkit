"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0194 import BranchRestrictionPolicyType
from .group_0192 import ProtectedBranchPullRequestReviewType


class BranchProtectionType(TypedDict):
    """Branch Protection

    Branch Protection
    """

    url: NotRequired[str]
    enabled: NotRequired[bool]
    required_status_checks: NotRequired[ProtectedBranchRequiredStatusCheckType]
    enforce_admins: NotRequired[ProtectedBranchAdminEnforcedType]
    required_pull_request_reviews: NotRequired[ProtectedBranchPullRequestReviewType]
    restrictions: NotRequired[BranchRestrictionPolicyType]
    required_linear_history: NotRequired[BranchProtectionPropRequiredLinearHistoryType]
    allow_force_pushes: NotRequired[BranchProtectionPropAllowForcePushesType]
    allow_deletions: NotRequired[BranchProtectionPropAllowDeletionsType]
    block_creations: NotRequired[BranchProtectionPropBlockCreationsType]
    required_conversation_resolution: NotRequired[
        BranchProtectionPropRequiredConversationResolutionType
    ]
    name: NotRequired[str]
    protection_url: NotRequired[str]
    required_signatures: NotRequired[BranchProtectionPropRequiredSignaturesType]
    lock_branch: NotRequired[BranchProtectionPropLockBranchType]
    allow_fork_syncing: NotRequired[BranchProtectionPropAllowForkSyncingType]


class ProtectedBranchAdminEnforcedType(TypedDict):
    """Protected Branch Admin Enforced

    Protected Branch Admin Enforced
    """

    url: str
    enabled: bool


class BranchProtectionPropRequiredLinearHistoryType(TypedDict):
    """BranchProtectionPropRequiredLinearHistory"""

    enabled: NotRequired[bool]


class BranchProtectionPropAllowForcePushesType(TypedDict):
    """BranchProtectionPropAllowForcePushes"""

    enabled: NotRequired[bool]


class BranchProtectionPropAllowDeletionsType(TypedDict):
    """BranchProtectionPropAllowDeletions"""

    enabled: NotRequired[bool]


class BranchProtectionPropBlockCreationsType(TypedDict):
    """BranchProtectionPropBlockCreations"""

    enabled: NotRequired[bool]


class BranchProtectionPropRequiredConversationResolutionType(TypedDict):
    """BranchProtectionPropRequiredConversationResolution"""

    enabled: NotRequired[bool]


class BranchProtectionPropRequiredSignaturesType(TypedDict):
    """BranchProtectionPropRequiredSignatures"""

    url: str
    enabled: bool


class BranchProtectionPropLockBranchType(TypedDict):
    """BranchProtectionPropLockBranch

    Whether to set the branch as read-only. If this is true, users will not be able
    to push to the branch.
    """

    enabled: NotRequired[bool]


class BranchProtectionPropAllowForkSyncingType(TypedDict):
    """BranchProtectionPropAllowForkSyncing

    Whether users can pull changes from upstream when the branch is locked. Set to
    `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    """

    enabled: NotRequired[bool]


class ProtectedBranchRequiredStatusCheckType(TypedDict):
    """Protected Branch Required Status Check

    Protected Branch Required Status Check
    """

    url: NotRequired[str]
    enforcement_level: NotRequired[str]
    contexts: list[str]
    checks: list[ProtectedBranchRequiredStatusCheckPropChecksItemsType]
    contexts_url: NotRequired[str]
    strict: NotRequired[bool]


class ProtectedBranchRequiredStatusCheckPropChecksItemsType(TypedDict):
    """ProtectedBranchRequiredStatusCheckPropChecksItems"""

    context: str
    app_id: Union[int, None]


__all__ = (
    "BranchProtectionType",
    "ProtectedBranchAdminEnforcedType",
    "BranchProtectionPropRequiredLinearHistoryType",
    "BranchProtectionPropAllowForcePushesType",
    "BranchProtectionPropAllowDeletionsType",
    "BranchProtectionPropBlockCreationsType",
    "BranchProtectionPropRequiredConversationResolutionType",
    "BranchProtectionPropRequiredSignaturesType",
    "BranchProtectionPropLockBranchType",
    "BranchProtectionPropAllowForkSyncingType",
    "ProtectedBranchRequiredStatusCheckType",
    "ProtectedBranchRequiredStatusCheckPropChecksItemsType",
)
