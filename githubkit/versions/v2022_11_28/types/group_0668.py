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
from .group_0383 import EnterpriseWebhooksType
from .group_0384 import SimpleInstallationType
from .group_0386 import RepositoryWebhooksType
from .group_0385 import OrganizationSimpleWebhooksType


class WebhookPullRequestReviewRequestRemovedOneof1Type(TypedDict):
    """WebhookPullRequestReviewRequestRemovedOneof1"""

    action: Literal["review_request_removed"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestType
    repository: RepositoryWebhooksType
    requested_team: WebhookPullRequestReviewRequestRemovedOneof1PropRequestedTeamType
    sender: SimpleUserType


class WebhookPullRequestReviewRequestRemovedOneof1PropRequestedTeamType(TypedDict):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof1PropRequestedTeamPropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof1PropRequestedTeamPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropRequestedTeamPropParent"""

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestType(TypedDict):
    """Pull Request"""

    links: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksType
    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ]
    additions: NotRequired[int]
    assignee: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAssigneeType,
        None,
    ]
    assignees: list[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAssigneesItemsType,
            None,
        ]
    ]
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
    auto_merge: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAutoMergeType,
        None,
    ]
    base: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBaseType
    body: Union[str, None]
    changed_files: NotRequired[int]
    closed_at: Union[datetime, None]
    comments: NotRequired[int]
    comments_url: str
    commits: NotRequired[int]
    commits_url: str
    created_at: datetime
    deletions: NotRequired[int]
    diff_url: str
    draft: bool
    head: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadType
    html_url: str
    id: int
    issue_url: str
    labels: list[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLabelsItemsType
    ]
    locked: bool
    maintainer_can_modify: NotRequired[bool]
    merge_commit_sha: Union[str, None]
    mergeable: NotRequired[Union[bool, None]]
    mergeable_state: NotRequired[str]
    merged: NotRequired[Union[bool, None]]
    merged_at: Union[datetime, None]
    merged_by: NotRequired[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMergedByType,
            None,
        ]
    ]
    milestone: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMilestoneType,
        None,
    ]
    node_id: str
    number: int
    patch_url: str
    rebaseable: NotRequired[Union[bool, None]]
    requested_reviewers: list[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof0Type,
            None,
            WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof1Type,
        ]
    ]
    requested_teams: list[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedTeamsItemsType
    ]
    review_comment_url: str
    review_comments: NotRequired[int]
    review_comments_url: str
    state: Literal["open", "closed"]
    statuses_url: str
    title: str
    updated_at: datetime
    url: str
    user: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropUserType, None
    ]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAssigneeType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAssigneesItemsType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAutoMergeType(
    TypedDict
):
    """PullRequestAutoMerge

    The status of auto merging a pull request.
    """

    commit_message: Union[str, None]
    commit_title: Union[str, None]
    enabled_by: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAutoMergePropEnabledByType,
        None,
    ]
    merge_method: Literal["merge", "squash", "rebase"]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAutoMergePropEnabledByType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLabelsItemsType(
    TypedDict
):
    """Label"""

    color: str
    default: bool
    description: Union[str, None]
    id: int
    name: str
    node_id: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMergedByType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMilestoneType(
    TypedDict
):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None]
    closed_issues: int
    created_at: datetime
    creator: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMilestonePropCreatorType,
        None,
    ]
    description: Union[str, None]
    due_on: Union[datetime, None]
    html_url: str
    id: int
    labels_url: str
    node_id: str
    number: int
    open_issues: int
    state: Literal["open", "closed"]
    title: str
    updated_at: datetime
    url: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMilestonePropCreatorType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof0Type(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinks"""

    comments: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropCommentsType
    commits: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropCommitsType
    html: (
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropHtmlType
    )
    issue: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropIssueType
    review_comment: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropReviewCommentType
    review_comments: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropReviewCommentsType
    self_: (
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropSelfType
    )
    statuses: WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropStatusesType


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropCommitsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropHtmlType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropIssueType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropReviewCommentType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropReviewCommentsType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropSelfType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropStatusesType(
    TypedDict
):
    """Link"""

    href: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBaseType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBase"""

    label: str
    ref: str
    repo: (
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoType
    )
    sha: str
    user: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropUserType,
        None,
    ]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoType(
    TypedDict
):
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
    license_: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
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
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropP
    ermissions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHead"""

    label: str
    ref: str
    repo: (
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoType
    )
    sha: str
    user: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropUserType,
        None,
    ]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropUserType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoType(
    TypedDict
):
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
    license_: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropLicenseType,
        None,
    ]
    master_branch: NotRequired[str]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merges_url: str
    milestones_url: str
    mirror_url: Union[str, None]
    name: str
    node_id: str
    notifications_url: str
    open_issues: int
    open_issues_count: int
    organization: NotRequired[str]
    owner: Union[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropOwnerType,
        None,
    ]
    permissions: NotRequired[
        WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropPermissionsType
    ]
    private: bool
    public: NotRequired[bool]
    pulls_url: str
    pushed_at: Union[int, datetime, None]
    releases_url: str
    role_name: NotRequired[Union[str, None]]
    size: int
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
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
    use_squash_pr_title_as_default: NotRequired[bool]
    visibility: Literal["public", "private", "internal"]
    watchers: int
    watchers_count: int
    web_commit_signoff_required: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropLicenseType(
    TypedDict
):
    """License"""

    key: str
    name: str
    node_id: str
    spdx_id: str
    url: Union[str, None]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropOwnerType(
    TypedDict
):
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


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropPermissionsType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropP
    ermissions
    """

    admin: bool
    maintain: NotRequired[bool]
    pull: bool
    push: bool
    triage: NotRequired[bool]


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof1Type(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof1PropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof1PropParentType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewer
    sItemsOneof1PropParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedTeamsItemsType(
    TypedDict
):
    """Team

    Groups of organization members that gives permissions on specified repositories.
    """

    deleted: NotRequired[bool]
    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    parent: NotRequired[
        Union[
            WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedTeamsItemsPropParentType,
            None,
        ]
    ]
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


class WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedTeamsItemsPropParentType(
    TypedDict
):
    """WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedTeamsIte
    msPropParent
    """

    description: Union[str, None]
    html_url: str
    id: int
    members_url: str
    name: str
    node_id: str
    permission: str
    privacy: Literal["open", "closed", "secret"]
    repositories_url: str
    slug: str
    url: str


__all__ = (
    "WebhookPullRequestReviewRequestRemovedOneof1Type",
    "WebhookPullRequestReviewRequestRemovedOneof1PropRequestedTeamType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropRequestedTeamPropParentType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAssigneeType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAssigneesItemsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAutoMergeType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropAutoMergePropEnabledByType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLabelsItemsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMergedByType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMilestoneType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropMilestonePropCreatorType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof0Type",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropUserType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropCommentsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropCommitsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropHtmlType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropIssueType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropReviewCommentType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropReviewCommentsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropSelfType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropLinksPropStatusesType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBaseType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropUserType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropLicenseType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropOwnerType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropBasePropRepoPropPermissionsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropUserType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropLicenseType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropOwnerType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropHeadPropRepoPropPermissionsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof1Type",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedReviewersItemsOneof1PropParentType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedTeamsItemsType",
    "WebhookPullRequestReviewRequestRemovedOneof1PropPullRequestPropRequestedTeamsItemsPropParentType",
)
