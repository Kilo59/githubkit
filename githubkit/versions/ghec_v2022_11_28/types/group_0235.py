"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0234 import BranchProtectionType


class ShortBranchType(TypedDict):
    """Short Branch

    Short Branch
    """

    name: str
    commit: ShortBranchPropCommitType
    protected: bool
    protection: NotRequired[BranchProtectionType]
    protection_url: NotRequired[str]


class ShortBranchPropCommitType(TypedDict):
    """ShortBranchPropCommit"""

    sha: str
    url: str


__all__ = (
    "ShortBranchPropCommitType",
    "ShortBranchType",
)
