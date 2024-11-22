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

from .group_0002 import SimpleUser


class GistCommit(GitHubModel):
    """Gist Commit

    Gist Commit
    """

    url: str = Field()
    version: str = Field()
    user: Union[None, SimpleUser] = Field()
    change_status: GistCommitPropChangeStatus = Field()
    committed_at: datetime = Field()


class GistCommitPropChangeStatus(GitHubModel):
    """GistCommitPropChangeStatus"""

    total: Missing[int] = Field(default=UNSET)
    additions: Missing[int] = Field(default=UNSET)
    deletions: Missing[int] = Field(default=UNSET)


model_rebuild(GistCommit)
model_rebuild(GistCommitPropChangeStatus)

__all__ = (
    "GistCommit",
    "GistCommitPropChangeStatus",
)
