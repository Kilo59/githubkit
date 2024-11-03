"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0420 import EnterpriseWebhooksType
from .group_0421 import SimpleInstallationType
from .group_0422 import OrganizationSimpleWebhooksType


class WebhookPushType(TypedDict):
    """push event"""

    after: str
    base_ref: Union[str, None]
    before: str
    commits: list[WebhookPushPropCommitsItemsType]
    compare: str
    created: bool
    deleted: bool
    enterprise: NotRequired[EnterpriseWebhooksType]
    forced: bool
    head_commit: Union[WebhookPushPropHeadCommitType, None]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pusher: WebhookPushPropPusherType
    ref: str
    repository: WebhookPushPropRepositoryType
    sender: NotRequired[SimpleUserType]


class WebhookPushPropHeadCommitType(TypedDict):
    """Commit"""

    added: NotRequired[list[str]]
    author: WebhookPushPropHeadCommitPropAuthorType
    committer: WebhookPushPropHeadCommitPropCommitterType
    distinct: bool
    id: str
    message: str
    modified: NotRequired[list[str]]
    removed: NotRequired[list[str]]
    timestamp: datetime
    tree_id: str
    url: str


class WebhookPushPropHeadCommitPropAuthorType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookPushPropHeadCommitPropCommitterType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookPushPropPusherType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: NotRequired[Union[str, None]]
    name: str
    username: NotRequired[str]


class WebhookPushPropCommitsItemsType(TypedDict):
    """Commit"""

    added: NotRequired[list[str]]
    author: WebhookPushPropCommitsItemsPropAuthorType
    committer: WebhookPushPropCommitsItemsPropCommitterType
    distinct: bool
    id: str
    message: str
    modified: NotRequired[list[str]]
    removed: NotRequired[list[str]]
    timestamp: datetime
    tree_id: str
    url: str


class WebhookPushPropCommitsItemsPropAuthorType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookPushPropCommitsItemsPropCommitterType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookPushPropRepositoryType(TypedDict):
    """Repository

    A git repository
    """

    allow_auto_merge: NotRequired[bool]
    allow_forking: NotRequired[bool]
    allow_merge_commit: NotRequired[bool]
    allow_rebase_merge: NotRequired[bool]
    allow_squash_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    archive_url: str
    archived: bool
    assignees_url: str
    blobs_url: str
    branches_url: str
    clone_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    created_at: Union[int, datetime]
    custom_properties: NotRequired[WebhookPushPropRepositoryPropCustomPropertiesType]
    default_branch: str
    delete_branch_on_merge: NotRequired[bool]
    deployments_url: str
    description: Union[str, None]
    disabled: NotRequired[bool]
    downloads_url: str
    events_url: str
    fork: bool
    forks: int
    forks_count: int
    forks_url: str
    full_name: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    has_downloads: bool
    has_issues: bool
    has_pages: bool
    has_projects: bool
    has_wiki: bool
    has_discussions: bool
    homepage: Union[str, None]
    hooks_url: str
    html_url: str
    id: int
    is_template: NotRequired[bool]
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    language: Union[str, None]
    languages_url: str
    license_: Union[WebhookPushPropRepositoryPropLicenseType, None]
    master_branch: NotRequired[str]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[WebhookPushPropRepositoryPropOwnerType, None]
    permissions: NotRequired[WebhookPushPropRepositoryPropPermissionsType]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    ssh_url: str
    stargazers: NotRequired[int]
    stargazers_count: int
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    svn_url: str
    tags_url: str
    teams_url: str
    topics: list[str]
    trees_url: str
    updated_at: datetime
    url: str
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPushPropRepositoryPropCustomPropertiesType(TypedDict):
    """WebhookPushPropRepositoryPropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


class WebhookPushPropRepositoryPropLicenseType(TypedDict):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPushPropRepositoryPropOwnerType(TypedDict):
    """User"""

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
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


class WebhookPushPropRepositoryPropPermissionsType(TypedDict):
    """WebhookPushPropRepositoryPropPermissions"""

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


__all__ = (
    "WebhookPushType",
    "WebhookPushPropHeadCommitType",
    "WebhookPushPropHeadCommitPropAuthorType",
    "WebhookPushPropHeadCommitPropCommitterType",
    "WebhookPushPropPusherType",
    "WebhookPushPropCommitsItemsType",
    "WebhookPushPropCommitsItemsPropAuthorType",
    "WebhookPushPropCommitsItemsPropCommitterType",
    "WebhookPushPropRepositoryType",
    "WebhookPushPropRepositoryPropCustomPropertiesType",
    "WebhookPushPropRepositoryPropLicenseType",
    "WebhookPushPropRepositoryPropOwnerType",
    "WebhookPushPropRepositoryPropPermissionsType",
)
