"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0211 import GitUserType
from .group_0212 import VerificationType


class CommitPropCommitType(TypedDict):
    """CommitPropCommit"""

    url: str
    author: Union[None, GitUserType]
    committer: Union[None, GitUserType]
    message: str
    comment_count: int
    tree: CommitPropCommitPropTreeType
    verification: NotRequired[VerificationType]


class CommitPropCommitPropTreeType(TypedDict):
    """CommitPropCommitPropTree"""

    sha: str
    url: str


__all__ = (
    "CommitPropCommitType",
    "CommitPropCommitPropTreeType",
)
