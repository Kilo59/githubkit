"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0001 import SimpleUser
from .group_0038 import ReactionRollup


class CommitComment(GitHubModel):
    """Commit Comment

    Commit Comment
    """

    html_url: str = Field()
    url: str = Field()
    id: int = Field()
    node_id: str = Field()
    body: str = Field()
    path: Union[str, None] = Field()
    position: Union[int, None] = Field()
    line: Union[int, None] = Field()
    commit_id: str = Field()
    user: Union[None, SimpleUser] = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ] = Field(
        title="author_association",
        description="How the author is associated with the repository.",
    )
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")


class TimelineCommitCommentedEvent(GitHubModel):
    """Timeline Commit Commented Event

    Timeline Commit Commented Event
    """

    event: Missing[Literal["commit_commented"]] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    commit_id: Missing[str] = Field(default=UNSET)
    comments: Missing[List[CommitComment]] = Field(default=UNSET)


model_rebuild(CommitComment)
model_rebuild(TimelineCommitCommentedEvent)

__all__ = (
    "CommitComment",
    "TimelineCommitCommentedEvent",
)
