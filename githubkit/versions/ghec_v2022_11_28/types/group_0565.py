"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0573 import WebhookIssueCommentCreatedPropIssueMergedMilestoneType
from .group_0574 import (
    WebhookIssueCommentCreatedPropIssueMergedPerformedViaGithubAppType,
)
from .group_0567 import (
    WebhookIssueCommentCreatedPropIssueAllof0PropAssigneeType,
    WebhookIssueCommentCreatedPropIssueAllof0PropLabelsItemsType,
    WebhookIssueCommentCreatedPropIssueAllof0PropPullRequestType,
)


class WebhookIssueCommentCreatedPropIssueType(TypedDict):
    """WebhookIssueCommentCreatedPropIssue

    The [issue](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/issues#get-an-issue) the comment belongs to.
    """

    active_lock_reason: Union[
        Literal["resolved", "off-topic", "too heated", "spam"], None
    ]
    assignee: Union[
        Union[WebhookIssueCommentCreatedPropIssueAllof0PropAssigneeType, None], None
    ]
    assignees: list[WebhookIssueCommentCreatedPropIssueMergedAssigneesType]
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
    body: Union[Union[str, None], None]
    closed_at: Union[datetime, None]
    comments: int
    comments_url: str
    created_at: datetime
    draft: NotRequired[bool]
    events_url: str
    html_url: str
    id: int
    labels: list[WebhookIssueCommentCreatedPropIssueAllof0PropLabelsItemsType]
    labels_url: str
    locked: bool
    milestone: Union[WebhookIssueCommentCreatedPropIssueMergedMilestoneType, None]
    node_id: str
    number: int
    performed_via_github_app: NotRequired[
        Union[WebhookIssueCommentCreatedPropIssueMergedPerformedViaGithubAppType, None]
    ]
    pull_request: NotRequired[
        WebhookIssueCommentCreatedPropIssueAllof0PropPullRequestType
    ]
    reactions: WebhookIssueCommentCreatedPropIssueMergedReactionsType
    repository_url: str
    state: Literal["open", "closed"]
    state_reason: NotRequired[Union[str, None]]
    timeline_url: NotRequired[str]
    title: str
    updated_at: datetime
    url: str
    user: WebhookIssueCommentCreatedPropIssueMergedUserType


class WebhookIssueCommentCreatedPropIssueMergedAssigneesType(TypedDict):
    """WebhookIssueCommentCreatedPropIssueMergedAssignees"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookIssueCommentCreatedPropIssueMergedReactionsType(TypedDict):
    """WebhookIssueCommentCreatedPropIssueMergedReactions"""

    plus_one: int
    minus_one: int
    confused: int
    eyes: int
    heart: int
    hooray: int
    laugh: int
    rocket: int
    total_count: int
    url: str


class WebhookIssueCommentCreatedPropIssueMergedUserType(TypedDict):
    """WebhookIssueCommentCreatedPropIssueMergedUser"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookIssueCommentCreatedPropIssueType",
    "WebhookIssueCommentCreatedPropIssueMergedAssigneesType",
    "WebhookIssueCommentCreatedPropIssueMergedReactionsType",
    "WebhookIssueCommentCreatedPropIssueMergedUserType",
)
