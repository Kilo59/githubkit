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

from .group_0578 import WebhookIssueCommentEditedPropIssueAllof0PropMilestone
from .group_0580 import (
    WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubApp,
)
from .group_0576 import (
    WebhookIssueCommentEditedPropIssueAllof0PropAssignee,
    WebhookIssueCommentEditedPropIssueAllof0PropLabelsItems,
    WebhookIssueCommentEditedPropIssueAllof0PropPullRequest,
)


class WebhookIssueCommentEditedPropIssueAllof0(GitHubModel):
    """Issue

    The [issue](https://docs.github.com/enterprise-
    cloud@latest//rest/issues/issues#get-an-issue) itself.
    """

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ] = Field()
    assignee: Missing[
        Union[WebhookIssueCommentEditedPropIssueAllof0PropAssignee, None]
    ] = Field(default=UNSET, title="User")
    assignees: List[
        Union[WebhookIssueCommentEditedPropIssueAllof0PropAssigneesItems, None]
    ] = Field()
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
        title="AuthorAssociation",
        description="How the author is associated with the repository.",
    )
    body: Union[str, None] = Field(description="Contents of the issue")
    closed_at: Union[datetime, None] = Field()
    comments: int = Field()
    comments_url: str = Field()
    created_at: datetime = Field()
    draft: Missing[bool] = Field(default=UNSET)
    events_url: str = Field()
    html_url: str = Field()
    id: int = Field()
    labels: Missing[List[WebhookIssueCommentEditedPropIssueAllof0PropLabelsItems]] = (
        Field(default=UNSET)
    )
    labels_url: str = Field()
    locked: Missing[bool] = Field(default=UNSET)
    milestone: Union[WebhookIssueCommentEditedPropIssueAllof0PropMilestone, None] = (
        Field(
            title="Milestone",
            description="A collection of related issues and pull requests.",
        )
    )
    node_id: str = Field()
    number: int = Field()
    performed_via_github_app: Missing[
        Union[WebhookIssueCommentEditedPropIssueAllof0PropPerformedViaGithubApp, None]
    ] = Field(
        default=UNSET,
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    pull_request: Missing[WebhookIssueCommentEditedPropIssueAllof0PropPullRequest] = (
        Field(default=UNSET)
    )
    reactions: WebhookIssueCommentEditedPropIssueAllof0PropReactions = Field(
        title="Reactions"
    )
    repository_url: str = Field()
    state: Missing[Literal["open", "closed"]] = Field(
        default=UNSET, description="State of the issue; either 'open' or 'closed'"
    )
    state_reason: Missing[Union[str, None]] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    title: str = Field(description="Title of the issue")
    updated_at: datetime = Field()
    url: str = Field(description="URL for the issue")
    user: Union[WebhookIssueCommentEditedPropIssueAllof0PropUser, None] = Field(
        title="User"
    )


class WebhookIssueCommentEditedPropIssueAllof0PropAssigneesItems(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


class WebhookIssueCommentEditedPropIssueAllof0PropReactions(GitHubModel):
    """Reactions"""

    plus_one: int = Field(alias="+1")
    minus_one: int = Field(alias="-1")
    confused: int = Field()
    eyes: int = Field()
    heart: int = Field()
    hooray: int = Field()
    laugh: int = Field()
    rocket: int = Field()
    total_count: int = Field()
    url: str = Field()


class WebhookIssueCommentEditedPropIssueAllof0PropUser(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssueCommentEditedPropIssueAllof0)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof0PropAssigneesItems)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof0PropReactions)
model_rebuild(WebhookIssueCommentEditedPropIssueAllof0PropUser)

__all__ = (
    "WebhookIssueCommentEditedPropIssueAllof0",
    "WebhookIssueCommentEditedPropIssueAllof0PropAssigneesItems",
    "WebhookIssueCommentEditedPropIssueAllof0PropReactions",
    "WebhookIssueCommentEditedPropIssueAllof0PropUser",
)
