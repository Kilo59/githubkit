"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0008 import Integration
from .group_0019 import Repository
from .group_0074 import Milestone
from .group_0075 import ReactionRollup
from .group_0408 import SearchResultTextMatchesItems


class IssueSearchResultItem(GitHubModel):
    """Issue Search Result Item

    Issue Search Result Item
    """

    url: str = Field()
    repository_url: str = Field()
    labels_url: str = Field()
    comments_url: str = Field()
    events_url: str = Field()
    html_url: str = Field()
    id: int = Field()
    node_id: str = Field()
    number: int = Field()
    title: str = Field()
    locked: bool = Field()
    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    assignees: Missing[Union[list[SimpleUser], None]] = Field(default=UNSET)
    user: Union[None, SimpleUser] = Field()
    labels: list[IssueSearchResultItemPropLabelsItems] = Field()
    sub_issues_summary: Missing[IssueSearchResultItemPropSubIssuesSummary] = Field(
        default=UNSET, title="Sub-issues Summary"
    )
    state: str = Field()
    state_reason: Missing[Union[str, None]] = Field(default=UNSET)
    assignee: Union[None, SimpleUser] = Field()
    milestone: Union[None, Milestone] = Field()
    comments: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    closed_at: Union[datetime, None] = Field()
    text_matches: Missing[list[SearchResultTextMatchesItems]] = Field(
        default=UNSET, title="Search Result Text Matches"
    )
    pull_request: Missing[IssueSearchResultItemPropPullRequest] = Field(default=UNSET)
    body: Missing[str] = Field(default=UNSET)
    score: float = Field()
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
    draft: Missing[bool] = Field(default=UNSET)
    repository: Missing[Repository] = Field(
        default=UNSET, title="Repository", description="A repository on GitHub."
    )
    body_html: Missing[str] = Field(default=UNSET)
    body_text: Missing[str] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    performed_via_github_app: Missing[Union[None, Integration, None]] = Field(
        default=UNSET
    )
    reactions: Missing[ReactionRollup] = Field(default=UNSET, title="Reaction Rollup")


class IssueSearchResultItemPropLabelsItems(GitHubModel):
    """IssueSearchResultItemPropLabelsItems"""

    id: Missing[int] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    color: Missing[str] = Field(default=UNSET)
    default: Missing[bool] = Field(default=UNSET)
    description: Missing[Union[str, None]] = Field(default=UNSET)


class IssueSearchResultItemPropSubIssuesSummary(GitHubModel):
    """Sub-issues Summary"""

    total: int = Field()
    completed: int = Field()
    percent_completed: int = Field()


class IssueSearchResultItemPropPullRequest(GitHubModel):
    """IssueSearchResultItemPropPullRequest"""

    merged_at: Missing[Union[datetime, None]] = Field(default=UNSET)
    diff_url: Union[str, None] = Field()
    html_url: Union[str, None] = Field()
    patch_url: Union[str, None] = Field()
    url: Union[str, None] = Field()


class SearchIssuesGetResponse200(GitHubModel):
    """SearchIssuesGetResponse200"""

    total_count: int = Field()
    incomplete_results: bool = Field()
    items: list[IssueSearchResultItem] = Field()


model_rebuild(IssueSearchResultItem)
model_rebuild(IssueSearchResultItemPropLabelsItems)
model_rebuild(IssueSearchResultItemPropSubIssuesSummary)
model_rebuild(IssueSearchResultItemPropPullRequest)
model_rebuild(SearchIssuesGetResponse200)

__all__ = (
    "IssueSearchResultItem",
    "IssueSearchResultItemPropLabelsItems",
    "IssueSearchResultItemPropPullRequest",
    "IssueSearchResultItemPropSubIssuesSummary",
    "SearchIssuesGetResponse200",
)
