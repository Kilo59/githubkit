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
from .group_0384 import EnterpriseWebhooksType
from .group_0385 import SimpleInstallationType
from .group_0387 import RepositoryWebhooksType
from .group_0386 import OrganizationSimpleWebhooksType


class WebhookCheckSuiteCompletedType(TypedDict):
    """check_suite completed event"""

    action: Literal["completed"]
    check_suite: WebhookCheckSuiteCompletedPropCheckSuiteType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookCheckSuiteCompletedPropCheckSuiteType(TypedDict):
    """WebhookCheckSuiteCompletedPropCheckSuite

    The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite).
    """

    after: Union[str, None]
    app: WebhookCheckSuiteCompletedPropCheckSuitePropAppType
    before: Union[str, None]
    check_runs_url: str
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "timed_out",
            "action_required",
            "stale",
            "skipped",
            "startup_failure",
        ],
    ]
    created_at: datetime
    head_branch: Union[str, None]
    head_commit: WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitType
    head_sha: str
    id: int
    latest_check_runs_count: int
    node_id: str
    pull_requests: list[
        WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsType
    ]
    rerequestable: NotRequired[bool]
    runs_rerequestable: NotRequired[bool]
    status: Union[
        None, Literal["requested", "in_progress", "completed", "queued", "pending"]
    ]
    updated_at: datetime
    url: str


class WebhookCheckSuiteCompletedPropCheckSuitePropAppType(TypedDict):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None]
    description: Union[str, None]
    events: NotRequired[list[str]]
    external_url: Union[str, None]
    html_url: str
    id: Union[int, None]
    client_id: NotRequired[Union[str, None]]
    name: str
    node_id: str
    owner: Union[WebhookCheckSuiteCompletedPropCheckSuitePropAppPropOwnerType, None]
    permissions: NotRequired[
        WebhookCheckSuiteCompletedPropCheckSuitePropAppPropPermissionsType
    ]
    slug: NotRequired[str]
    updated_at: Union[datetime, None]


class WebhookCheckSuiteCompletedPropCheckSuitePropAppPropOwnerType(TypedDict):
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


class WebhookCheckSuiteCompletedPropCheckSuitePropAppPropPermissionsType(TypedDict):
    """WebhookCheckSuiteCompletedPropCheckSuitePropAppPropPermissions

    The set of permissions for the GitHub app
    """

    actions: NotRequired[Literal["read", "write"]]
    administration: NotRequired[Literal["read", "write"]]
    checks: NotRequired[Literal["read", "write"]]
    content_references: NotRequired[Literal["read", "write"]]
    contents: NotRequired[Literal["read", "write"]]
    deployments: NotRequired[Literal["read", "write"]]
    discussions: NotRequired[Literal["read", "write"]]
    emails: NotRequired[Literal["read", "write"]]
    environments: NotRequired[Literal["read", "write"]]
    issues: NotRequired[Literal["read", "write"]]
    keys: NotRequired[Literal["read", "write"]]
    members: NotRequired[Literal["read", "write"]]
    metadata: NotRequired[Literal["read", "write"]]
    organization_administration: NotRequired[Literal["read", "write"]]
    organization_hooks: NotRequired[Literal["read", "write"]]
    organization_packages: NotRequired[Literal["read", "write"]]
    organization_plan: NotRequired[Literal["read", "write"]]
    organization_projects: NotRequired[Literal["read", "write", "admin"]]
    organization_secrets: NotRequired[Literal["read", "write"]]
    organization_self_hosted_runners: NotRequired[Literal["read", "write"]]
    organization_user_blocking: NotRequired[Literal["read", "write"]]
    packages: NotRequired[Literal["read", "write"]]
    pages: NotRequired[Literal["read", "write"]]
    pull_requests: NotRequired[Literal["read", "write"]]
    repository_hooks: NotRequired[Literal["read", "write"]]
    repository_projects: NotRequired[Literal["read", "write", "admin"]]
    secret_scanning_alerts: NotRequired[Literal["read", "write"]]
    secrets: NotRequired[Literal["read", "write"]]
    security_events: NotRequired[Literal["read", "write"]]
    security_scanning_alert: NotRequired[Literal["read", "write"]]
    single_file: NotRequired[Literal["read", "write"]]
    statuses: NotRequired[Literal["read", "write"]]
    team_discussions: NotRequired[Literal["read", "write"]]
    vulnerability_alerts: NotRequired[Literal["read", "write"]]
    workflows: NotRequired[Literal["read", "write"]]


class WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitType(TypedDict):
    """SimpleCommit"""

    author: WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitPropAuthorType
    committer: WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitPropCommitterType
    id: str
    message: str
    timestamp: str
    tree_id: str


class WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitPropAuthorType(TypedDict):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitPropCommitterType(
    TypedDict
):
    """Committer

    Metaproperties for Git author/committer information.
    """

    date: NotRequired[datetime]
    email: Union[str, None]
    name: str
    username: NotRequired[str]


class WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsType(TypedDict):
    """Check Run Pull Request"""

    base: WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropBaseType
    head: WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropHeadType
    id: int
    number: int
    url: str


class WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropBaseType(
    TypedDict
):
    """WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropBase"""

    ref: str
    repo: WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropBasePropRepoType
    sha: str


class WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropBasePropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


class WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropHeadType(
    TypedDict
):
    """WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropHead"""

    ref: str
    repo: WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropHeadPropRepoType
    sha: str


class WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropHeadPropRepoType(
    TypedDict
):
    """Repo Ref"""

    id: int
    name: str
    url: str


__all__ = (
    "WebhookCheckSuiteCompletedType",
    "WebhookCheckSuiteCompletedPropCheckSuiteType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropAppType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropAppPropOwnerType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropAppPropPermissionsType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitPropAuthorType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropHeadCommitPropCommitterType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropBaseType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropBasePropRepoType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropHeadType",
    "WebhookCheckSuiteCompletedPropCheckSuitePropPullRequestsItemsPropHeadPropRepoType",
)
