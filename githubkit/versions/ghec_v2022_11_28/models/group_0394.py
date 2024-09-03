"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0211 import GitUser
from .group_0212 import Verification


class CommitSearchResultItemPropCommit(GitHubModel):
    """CommitSearchResultItemPropCommit"""

    author: CommitSearchResultItemPropCommitPropAuthor = Field()
    committer: Union[None, GitUser] = Field()
    comment_count: int = Field()
    message: str = Field()
    tree: CommitSearchResultItemPropCommitPropTree = Field()
    url: str = Field()
    verification: Missing[Verification] = Field(default=UNSET, title="Verification")


class CommitSearchResultItemPropCommitPropAuthor(GitHubModel):
    """CommitSearchResultItemPropCommitPropAuthor"""

    name: str = Field()
    email: str = Field()
    date: datetime = Field()


class CommitSearchResultItemPropCommitPropTree(GitHubModel):
    """CommitSearchResultItemPropCommitPropTree"""

    sha: str = Field()
    url: str = Field()


model_rebuild(CommitSearchResultItemPropCommit)
model_rebuild(CommitSearchResultItemPropCommitPropAuthor)
model_rebuild(CommitSearchResultItemPropCommitPropTree)

__all__ = (
    "CommitSearchResultItemPropCommit",
    "CommitSearchResultItemPropCommitPropAuthor",
    "CommitSearchResultItemPropCommitPropTree",
)
