"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0200 import GitUserType
from .group_0201 import VerificationType


class CommitSearchResultItemPropCommitType(TypedDict):
    """CommitSearchResultItemPropCommit"""

    author: CommitSearchResultItemPropCommitPropAuthorType
    committer: Union[None, GitUserType]
    comment_count: int
    message: str
    tree: CommitSearchResultItemPropCommitPropTreeType
    url: str
    verification: NotRequired[VerificationType]


class CommitSearchResultItemPropCommitPropAuthorType(TypedDict):
    """CommitSearchResultItemPropCommitPropAuthor"""

    name: str
    email: str
    date: datetime


class CommitSearchResultItemPropCommitPropTreeType(TypedDict):
    """CommitSearchResultItemPropCommitPropTree"""

    sha: str
    url: str


__all__ = (
    "CommitSearchResultItemPropCommitPropAuthorType",
    "CommitSearchResultItemPropCommitPropTreeType",
    "CommitSearchResultItemPropCommitType",
)
