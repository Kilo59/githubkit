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

from .group_0064 import Milestone
from .group_0249 import AutoMerge
from .group_0001 import SimpleUser
from .group_0047 import TeamSimple
from .group_0330 import PullRequestPropBase
from .group_0332 import PullRequestPropLinks
from .group_0329 import PullRequestPropHead, PullRequestPropLabelsItems


class PullRequest(GitHubModel):
    """Pull Request

    Pull requests let you tell others about changes you've pushed to a repository on
    GitHub. Once a pull request is sent, interested parties can review the set of
    changes, discuss potential modifications, and even push follow-up commits if
    necessary.
    """

    url: str = Field()
    id: int = Field()
    node_id: str = Field()
    html_url: str = Field()
    diff_url: str = Field()
    patch_url: str = Field()
    issue_url: str = Field()
    commits_url: str = Field()
    review_comments_url: str = Field()
    review_comment_url: str = Field()
    comments_url: str = Field()
    statuses_url: str = Field()
    number: int = Field(
        description="Number uniquely identifying the pull request within its repository."
    )
    state: Literal["open", "closed"] = Field(
        description="State of this Pull Request. Either `open` or `closed`."
    )
    locked: bool = Field()
    title: str = Field(description="The title of the pull request.")
    user: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    body: Union[str, None] = Field()
    labels: List[PullRequestPropLabelsItems] = Field()
    milestone: Union[None, Milestone] = Field()
    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    created_at: datetime = Field()
    updated_at: datetime = Field()
    closed_at: Union[datetime, None] = Field()
    merged_at: Union[datetime, None] = Field()
    merge_commit_sha: Union[str, None] = Field()
    assignee: Union[None, SimpleUser] = Field()
    assignees: Missing[Union[List[SimpleUser], None]] = Field(default=UNSET)
    requested_reviewers: Missing[Union[List[SimpleUser], None]] = Field(default=UNSET)
    requested_teams: Missing[Union[List[TeamSimple], None]] = Field(default=UNSET)
    head: PullRequestPropHead = Field()
    base: PullRequestPropBase = Field()
    links: PullRequestPropLinks = Field(alias="_links")
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
    auto_merge: Union[AutoMerge, None] = Field(
        title="Auto merge", description="The status of auto merging a pull request."
    )
    draft: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether or not the pull request is a draft.",
    )
    merged: bool = Field()
    mergeable: Union[bool, None] = Field()
    rebaseable: Missing[Union[bool, None]] = Field(default=UNSET)
    mergeable_state: str = Field()
    merged_by: Union[None, SimpleUser] = Field()
    comments: int = Field()
    review_comments: int = Field()
    maintainer_can_modify: bool = Field(
        description="Indicates whether maintainers can modify the pull request."
    )
    commits: int = Field()
    additions: int = Field()
    deletions: int = Field()
    changed_files: int = Field()


model_rebuild(PullRequest)

__all__ = ("PullRequest",)
