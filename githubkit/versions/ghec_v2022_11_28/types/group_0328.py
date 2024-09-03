"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0064 import MilestoneType
from .group_0249 import AutoMergeType
from .group_0001 import SimpleUserType
from .group_0047 import TeamSimpleType
from .group_0330 import PullRequestPropBaseType
from .group_0332 import PullRequestPropLinksType
from .group_0329 import PullRequestPropHeadType, PullRequestPropLabelsItemsType


class PullRequestType(TypedDict):
    """Pull Request

    Pull requests let you tell others about changes you've pushed to a repository on
    GitHub. Once a pull request is sent, interested parties can review the set of
    changes, discuss potential modifications, and even push follow-up commits if
    necessary.
    """

    url: str
    id: int
    node_id: str
    html_url: str
    diff_url: str
    patch_url: str
    issue_url: str
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    number: int
    state: Literal["open", "closed"]
    locked: bool
    title: str
    user: SimpleUserType
    body: Union[str, None]
    labels: List[PullRequestPropLabelsItemsType]
    milestone: Union[None, MilestoneType]
    active_lock_reason: NotRequired[Union[str, None]]
    created_at: datetime
    updated_at: datetime
    closed_at: Union[datetime, None]
    merged_at: Union[datetime, None]
    merge_commit_sha: Union[str, None]
    assignee: Union[None, SimpleUserType]
    assignees: NotRequired[Union[List[SimpleUserType], None]]
    requested_reviewers: NotRequired[Union[List[SimpleUserType], None]]
    requested_teams: NotRequired[Union[List[TeamSimpleType], None]]
    head: PullRequestPropHeadType
    base: PullRequestPropBaseType
    links: PullRequestPropLinksType
    author_association: Literal[
        "COLLABORATOR",
        "CONTRIBUTOR",
        "FIRST_TIMER",
        "FIRST_TIME_CONTRIBUTOR",
        "MANNEQUIN",
        "MEMBER",
        "NONE",
        "OWNER",
    ]
    auto_merge: Union[AutoMergeType, None]
    draft: NotRequired[bool]
    merged: bool
    mergeable: Union[bool, None]
    rebaseable: NotRequired[Union[bool, None]]
    mergeable_state: str
    merged_by: Union[None, SimpleUserType]
    comments: int
    review_comments: int
    maintainer_can_modify: bool
    commits: int
    additions: int
    deletions: int
    changed_files: int


__all__ = ("PullRequestType",)
