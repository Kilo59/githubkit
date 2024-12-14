"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0202 import DiffEntryType
from .group_0204 import CommitPropCommitType


class CommitType(TypedDict):
    """Commit

    Commit
    """

    url: str
    sha: str
    node_id: str
    html_url: str
    comments_url: str
    commit: CommitPropCommitType
    author: Union[SimpleUserType, EmptyObjectType, None]
    committer: Union[SimpleUserType, EmptyObjectType, None]
    parents: list[CommitPropParentsItemsType]
    stats: NotRequired[CommitPropStatsType]
    files: NotRequired[list[DiffEntryType]]


class EmptyObjectType(TypedDict):
    """Empty Object

    An object without any properties.
    """


class CommitPropParentsItemsType(TypedDict):
    """CommitPropParentsItems"""

    sha: str
    url: str
    html_url: NotRequired[str]


class CommitPropStatsType(TypedDict):
    """CommitPropStats"""

    additions: NotRequired[int]
    deletions: NotRequired[int]
    total: NotRequired[int]


__all__ = (
    "CommitPropParentsItemsType",
    "CommitPropStatsType",
    "CommitType",
    "EmptyObjectType",
)
