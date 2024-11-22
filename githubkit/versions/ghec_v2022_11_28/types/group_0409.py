"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0073 import MilestoneType
from .group_0002 import SimpleUserType
from .group_0019 import RepositoryType
from .group_0008 import IntegrationType
from .group_0074 import ReactionRollupType
from .group_0405 import SearchResultTextMatchesItemsType


class IssueSearchResultItemType(TypedDict):
    """Issue Search Result Item

    Issue Search Result Item
    """

    url: str
    repository_url: str
    labels_url: str
    comments_url: str
    events_url: str
    html_url: str
    id: int
    node_id: str
    number: int
    title: str
    locked: bool
    active_lock_reason: NotRequired[Union[str, None]]
    assignees: NotRequired[Union[list[SimpleUserType], None]]
    user: Union[None, SimpleUserType]
    labels: list[IssueSearchResultItemPropLabelsItemsType]
    state: str
    state_reason: NotRequired[Union[str, None]]
    assignee: Union[None, SimpleUserType]
    milestone: Union[None, MilestoneType]
    comments: int
    created_at: datetime
    updated_at: datetime
    closed_at: Union[datetime, None]
    text_matches: NotRequired[list[SearchResultTextMatchesItemsType]]
    pull_request: NotRequired[IssueSearchResultItemPropPullRequestType]
    body: NotRequired[str]
    score: float
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
    draft: NotRequired[bool]
    repository: NotRequired[RepositoryType]
    body_html: NotRequired[str]
    body_text: NotRequired[str]
    timeline_url: NotRequired[str]
    performed_via_github_app: NotRequired[Union[None, IntegrationType, None]]
    reactions: NotRequired[ReactionRollupType]


class IssueSearchResultItemPropLabelsItemsType(TypedDict):
    """IssueSearchResultItemPropLabelsItems"""

    id: NotRequired[int]
    node_id: NotRequired[str]
    url: NotRequired[str]
    name: NotRequired[str]
    color: NotRequired[str]
    default: NotRequired[bool]
    description: NotRequired[Union[str, None]]


class IssueSearchResultItemPropPullRequestType(TypedDict):
    """IssueSearchResultItemPropPullRequest"""

    merged_at: NotRequired[Union[datetime, None]]
    diff_url: Union[str, None]
    html_url: Union[str, None]
    patch_url: Union[str, None]
    url: Union[str, None]


class SearchIssuesGetResponse200Type(TypedDict):
    """SearchIssuesGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: list[IssueSearchResultItemType]


__all__ = (
    "IssueSearchResultItemType",
    "IssueSearchResultItemPropLabelsItemsType",
    "IssueSearchResultItemPropPullRequestType",
    "SearchIssuesGetResponse200Type",
)
