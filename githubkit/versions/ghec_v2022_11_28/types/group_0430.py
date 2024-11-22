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
from .group_0018 import LicenseSimpleType


class RepositoryWebhooksType(TypedDict):
    """Repository

    The repository on GitHub where the event occurred. Webhook payloads contain the
    `repository` property
    when the event occurs from activity in a repository.
    """

    id: int
    node_id: str
    name: str
    full_name: str
    license_: Union[None, LicenseSimpleType]
    organization: NotRequired[Union[None, SimpleUserType]]
    forks: int
    permissions: NotRequired[RepositoryWebhooksPropPermissionsType]
    owner: SimpleUserType
    private: bool
    html_url: str
    description: Union[str, None]
    fork: bool
    url: str
    archive_url: str
    assignees_url: str
    blobs_url: str
    branches_url: str
    collaborators_url: str
    comments_url: str
    commits_url: str
    compare_url: str
    contents_url: str
    contributors_url: str
    deployments_url: str
    downloads_url: str
    events_url: str
    forks_url: str
    git_commits_url: str
    git_refs_url: str
    git_tags_url: str
    git_url: str
    issue_comment_url: str
    issue_events_url: str
    issues_url: str
    keys_url: str
    labels_url: str
    languages_url: str
    merges_url: str
    milestones_url: str
    notifications_url: str
    pulls_url: str
    releases_url: str
    ssh_url: str
    stargazers_url: str
    statuses_url: str
    subscribers_url: str
    subscription_url: str
    tags_url: str
    teams_url: str
    trees_url: str
    clone_url: str
    mirror_url: Union[str, None]
    hooks_url: str
    svn_url: str
    homepage: Union[str, None]
    language: Union[str, None]
    forks_count: int
    stargazers_count: int
    watchers_count: int
    size: int
    default_branch: str
    open_issues_count: int
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    custom_properties: NotRequired[RepositoryWebhooksPropCustomPropertiesType]
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    has_pages: bool
    has_downloads: bool
    has_discussions: NotRequired[bool]
    archived: bool
    disabled: bool
    visibility: NotRequired[str]
    pushed_at: Union[datetime, None]
    created_at: Union[datetime, None]
    updated_at: Union[datetime, None]
    allow_rebase_merge: NotRequired[bool]
    template_repository: NotRequired[
        Union[RepositoryWebhooksPropTemplateRepositoryType, None]
    ]
    temp_clone_token: NotRequired[Union[str, None]]
    allow_squash_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    allow_merge_commit: NotRequired[bool]
    allow_forking: NotRequired[bool]
    web_commit_signoff_required: NotRequired[bool]
    subscribers_count: NotRequired[int]
    network_count: NotRequired[int]
    open_issues: int
    watchers: int
    master_branch: NotRequired[str]
    starred_at: NotRequired[str]
    anonymous_access_enabled: NotRequired[bool]


class RepositoryWebhooksPropPermissionsType(TypedDict):
    """RepositoryWebhooksPropPermissions"""

    admin: bool
    pull: bool
    triage: NotRequired[bool]
    push: bool
    maintain: NotRequired[bool]


class RepositoryWebhooksPropCustomPropertiesType(TypedDict):
    """RepositoryWebhooksPropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


class RepositoryWebhooksPropTemplateRepositoryType(TypedDict):
    """RepositoryWebhooksPropTemplateRepository"""

    id: NotRequired[int]
    node_id: NotRequired[str]
    name: NotRequired[str]
    full_name: NotRequired[str]
    owner: NotRequired[RepositoryWebhooksPropTemplateRepositoryPropOwnerType]
    private: NotRequired[bool]
    html_url: NotRequired[str]
    description: NotRequired[str]
    fork: NotRequired[bool]
    url: NotRequired[str]
    archive_url: NotRequired[str]
    assignees_url: NotRequired[str]
    blobs_url: NotRequired[str]
    branches_url: NotRequired[str]
    collaborators_url: NotRequired[str]
    comments_url: NotRequired[str]
    commits_url: NotRequired[str]
    compare_url: NotRequired[str]
    contents_url: NotRequired[str]
    contributors_url: NotRequired[str]
    deployments_url: NotRequired[str]
    downloads_url: NotRequired[str]
    events_url: NotRequired[str]
    forks_url: NotRequired[str]
    git_commits_url: NotRequired[str]
    git_refs_url: NotRequired[str]
    git_tags_url: NotRequired[str]
    git_url: NotRequired[str]
    issue_comment_url: NotRequired[str]
    issue_events_url: NotRequired[str]
    issues_url: NotRequired[str]
    keys_url: NotRequired[str]
    labels_url: NotRequired[str]
    languages_url: NotRequired[str]
    merges_url: NotRequired[str]
    milestones_url: NotRequired[str]
    notifications_url: NotRequired[str]
    pulls_url: NotRequired[str]
    releases_url: NotRequired[str]
    ssh_url: NotRequired[str]
    stargazers_url: NotRequired[str]
    statuses_url: NotRequired[str]
    subscribers_url: NotRequired[str]
    subscription_url: NotRequired[str]
    tags_url: NotRequired[str]
    teams_url: NotRequired[str]
    trees_url: NotRequired[str]
    clone_url: NotRequired[str]
    mirror_url: NotRequired[str]
    hooks_url: NotRequired[str]
    svn_url: NotRequired[str]
    homepage: NotRequired[str]
    language: NotRequired[str]
    forks_count: NotRequired[int]
    stargazers_count: NotRequired[int]
    watchers_count: NotRequired[int]
    size: NotRequired[int]
    default_branch: NotRequired[str]
    open_issues_count: NotRequired[int]
    is_template: NotRequired[bool]
    topics: NotRequired[list[str]]
    has_issues: NotRequired[bool]
    has_projects: NotRequired[bool]
    has_wiki: NotRequired[bool]
    has_pages: NotRequired[bool]
    has_downloads: NotRequired[bool]
    archived: NotRequired[bool]
    disabled: NotRequired[bool]
    visibility: NotRequired[str]
    pushed_at: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    permissions: NotRequired[
        RepositoryWebhooksPropTemplateRepositoryPropPermissionsType
    ]
    allow_rebase_merge: NotRequired[bool]
    temp_clone_token: NotRequired[Union[str, None]]
    allow_squash_merge: NotRequired[bool]
    allow_auto_merge: NotRequired[bool]
    delete_branch_on_merge: NotRequired[bool]
    allow_update_branch: NotRequired[bool]
    use_squash_pr_title_as_default: NotRequired[bool]
    squash_merge_commit_title: NotRequired[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]]
    squash_merge_commit_message: NotRequired[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ]
    merge_commit_title: NotRequired[Literal["PR_TITLE", "MERGE_MESSAGE"]]
    merge_commit_message: NotRequired[Literal["PR_BODY", "PR_TITLE", "BLANK"]]
    allow_merge_commit: NotRequired[bool]
    subscribers_count: NotRequired[int]
    network_count: NotRequired[int]


class RepositoryWebhooksPropTemplateRepositoryPropOwnerType(TypedDict):
    """RepositoryWebhooksPropTemplateRepositoryPropOwner"""

    login: NotRequired[str]
    id: NotRequired[int]
    node_id: NotRequired[str]
    avatar_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    url: NotRequired[str]
    html_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    organizations_url: NotRequired[str]
    repos_url: NotRequired[str]
    events_url: NotRequired[str]
    received_events_url: NotRequired[str]
    type: NotRequired[str]
    site_admin: NotRequired[bool]


class RepositoryWebhooksPropTemplateRepositoryPropPermissionsType(TypedDict):
    """RepositoryWebhooksPropTemplateRepositoryPropPermissions"""

    admin: NotRequired[bool]
    maintain: NotRequired[bool]
    push: NotRequired[bool]
    triage: NotRequired[bool]
    pull: NotRequired[bool]


__all__ = (
    "RepositoryWebhooksType",
    "RepositoryWebhooksPropPermissionsType",
    "RepositoryWebhooksPropCustomPropertiesType",
    "RepositoryWebhooksPropTemplateRepositoryType",
    "RepositoryWebhooksPropTemplateRepositoryPropOwnerType",
    "RepositoryWebhooksPropTemplateRepositoryPropPermissionsType",
)
