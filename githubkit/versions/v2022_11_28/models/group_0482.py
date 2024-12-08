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
from .group_0388 import EnterpriseWebhooks
from .group_0389 import SimpleInstallation
from .group_0390 import OrganizationSimpleWebhooks
from .group_0391 import RepositoryWebhooks
from .group_0396 import WebhooksWorkflow


class WebhookDeploymentStatusCreated(GitHubModel):
    """deployment_status created event"""

    action: Literal["created"] = Field()
    check_run: Missing[Union[WebhookDeploymentStatusCreatedPropCheckRun, None]] = Field(
        default=UNSET
    )
    deployment: WebhookDeploymentStatusCreatedPropDeployment = Field(
        title="Deployment",
        description="The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments).",
    )
    deployment_status: WebhookDeploymentStatusCreatedPropDeploymentStatus = Field(
        description="The [deployment status](https://docs.github.com/rest/deployments/statuses#list-deployment-statuses)."
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    workflow: Missing[Union[WebhooksWorkflow, None]] = Field(
        default=UNSET, title="Workflow"
    )
    workflow_run: Missing[
        Union[WebhookDeploymentStatusCreatedPropWorkflowRun, None]
    ] = Field(default=UNSET, title="Deployment Workflow Run")


class WebhookDeploymentStatusCreatedPropCheckRun(GitHubModel):
    """WebhookDeploymentStatusCreatedPropCheckRun"""

    completed_at: Union[datetime, None] = Field()
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
        ],
    ] = Field(
        description="The result of the completed check run. This value will be `null` until the check run has completed."
    )
    details_url: str = Field()
    external_id: str = Field()
    head_sha: str = Field(description="The SHA of the commit that is being checked.")
    html_url: str = Field()
    id: int = Field(description="The id of the check.")
    name: str = Field(description="The name of the check run.")
    node_id: str = Field()
    started_at: datetime = Field()
    status: Literal["queued", "in_progress", "completed", "waiting", "pending"] = Field(
        description="The current status of the check run. Can be `queued`, `in_progress`, or `completed`."
    )
    url: str = Field()


class WebhookDeploymentStatusCreatedPropDeployment(GitHubModel):
    """Deployment

    The [deployment](https://docs.github.com/rest/deployments/deployments#list-
    deployments).
    """

    created_at: str = Field()
    creator: Union[WebhookDeploymentStatusCreatedPropDeploymentPropCreator, None] = (
        Field(title="User")
    )
    description: Union[str, None] = Field()
    environment: str = Field()
    id: int = Field()
    node_id: str = Field()
    original_environment: str = Field()
    payload: Union[
        str, WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1, None
    ] = Field()
    performed_via_github_app: Missing[
        Union[
            WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubApp, None
        ]
    ] = Field(
        default=UNSET,
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    production_environment: Missing[bool] = Field(default=UNSET)
    ref: str = Field()
    repository_url: str = Field()
    sha: str = Field()
    statuses_url: str = Field()
    task: str = Field()
    transient_environment: Missing[bool] = Field(default=UNSET)
    updated_at: str = Field()
    url: str = Field()


class WebhookDeploymentStatusCreatedPropDeploymentPropCreator(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1(GitHubModel):
    """WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1"""


class WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubApp(
    GitHubModel
):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[list[str]] = Field(
        default=UNSET, description="The list of events for the GitHub app"
    )
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropOwner,
        None,
    ] = Field(title="User")
    permissions: Missing[
        WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


class WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropOwner(
    GitHubModel
):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions(
    GitHubModel
):
    """WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermiss
    ions

    The set of permissions for the GitHub app
    """

    actions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    administration: Missing[Literal["read", "write"]] = Field(default=UNSET)
    checks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    content_references: Missing[Literal["read", "write"]] = Field(default=UNSET)
    contents: Missing[Literal["read", "write"]] = Field(default=UNSET)
    deployments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    emails: Missing[Literal["read", "write"]] = Field(default=UNSET)
    environments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    issues: Missing[Literal["read", "write"]] = Field(default=UNSET)
    keys: Missing[Literal["read", "write"]] = Field(default=UNSET)
    members: Missing[Literal["read", "write"]] = Field(default=UNSET)
    metadata: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_administration: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_plan: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_self_hosted_runners: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_user_blocking: Missing[Literal["read", "write"]] = Field(default=UNSET)
    packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pull_requests: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secret_scanning_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_events: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_scanning_alert: Missing[Literal["read", "write"]] = Field(default=UNSET)
    single_file: Missing[Literal["read", "write"]] = Field(default=UNSET)
    statuses: Missing[Literal["read", "write"]] = Field(default=UNSET)
    team_discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    vulnerability_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    workflows: Missing[Literal["read", "write"]] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropDeploymentStatus(GitHubModel):
    """WebhookDeploymentStatusCreatedPropDeploymentStatus

    The [deployment status](https://docs.github.com/rest/deployments/statuses#list-
    deployment-statuses).
    """

    created_at: str = Field()
    creator: Union[
        WebhookDeploymentStatusCreatedPropDeploymentStatusPropCreator, None
    ] = Field(title="User")
    deployment_url: str = Field()
    description: str = Field(
        description="The optional human-readable description added to the status."
    )
    environment: str = Field()
    environment_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    log_url: Missing[str] = Field(default=UNSET)
    node_id: str = Field()
    performed_via_github_app: Missing[
        Union[
            WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubApp,
            None,
        ]
    ] = Field(
        default=UNSET,
        title="App",
        description="GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.",
    )
    repository_url: str = Field()
    state: str = Field(
        description="The new state. Can be `pending`, `success`, `failure`, or `error`."
    )
    target_url: str = Field(description="The optional link added to the status.")
    updated_at: str = Field()
    url: str = Field()


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropCreator(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubApp(
    GitHubModel
):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[list[str]] = Field(
        default=UNSET, description="The list of events for the GitHub app"
    )
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropOwner,
        None,
    ] = Field(title="User")
    permissions: Missing[
        WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropOwner(
    GitHubModel
):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropPermissions(
    GitHubModel
):
    """WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropP
    ermissions

    The set of permissions for the GitHub app
    """

    actions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    administration: Missing[Literal["read", "write"]] = Field(default=UNSET)
    checks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    content_references: Missing[Literal["read", "write"]] = Field(default=UNSET)
    contents: Missing[Literal["read", "write"]] = Field(default=UNSET)
    deployments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    emails: Missing[Literal["read", "write"]] = Field(default=UNSET)
    environments: Missing[Literal["read", "write"]] = Field(default=UNSET)
    issues: Missing[Literal["read", "write"]] = Field(default=UNSET)
    keys: Missing[Literal["read", "write"]] = Field(default=UNSET)
    members: Missing[Literal["read", "write"]] = Field(default=UNSET)
    metadata: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_administration: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_plan: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    organization_self_hosted_runners: Missing[Literal["read", "write"]] = Field(
        default=UNSET
    )
    organization_user_blocking: Missing[Literal["read", "write"]] = Field(default=UNSET)
    packages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pages: Missing[Literal["read", "write"]] = Field(default=UNSET)
    pull_requests: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_hooks: Missing[Literal["read", "write"]] = Field(default=UNSET)
    repository_projects: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secret_scanning_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    secrets: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_events: Missing[Literal["read", "write"]] = Field(default=UNSET)
    security_scanning_alert: Missing[Literal["read", "write"]] = Field(default=UNSET)
    single_file: Missing[Literal["read", "write"]] = Field(default=UNSET)
    statuses: Missing[Literal["read", "write"]] = Field(default=UNSET)
    team_discussions: Missing[Literal["read", "write"]] = Field(default=UNSET)
    vulnerability_alerts: Missing[Literal["read", "write"]] = Field(default=UNSET)
    workflows: Missing[Literal["read", "write"]] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRun(GitHubModel):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentStatusCreatedPropWorkflowRunPropActor, None] = Field(
        title="User"
    )
    artifacts_url: Missing[str] = Field(default=UNSET)
    cancel_url: Missing[str] = Field(default=UNSET)
    check_suite_id: int = Field()
    check_suite_node_id: str = Field()
    check_suite_url: Missing[str] = Field(default=UNSET)
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
            "startup_failure",
        ],
    ] = Field()
    created_at: datetime = Field()
    display_title: str = Field()
    event: str = Field()
    head_branch: str = Field()
    head_commit: Missing[None] = Field(default=UNSET)
    head_repository: Missing[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepository
    ] = Field(default=UNSET)
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    jobs_url: Missing[str] = Field(default=UNSET)
    logs_url: Missing[str] = Field(default=UNSET)
    name: str = Field()
    node_id: str = Field()
    path: str = Field()
    previous_attempt_url: Missing[None] = Field(default=UNSET)
    pull_requests: list[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItems
    ] = Field()
    referenced_workflows: Missing[
        Union[
            list[
                WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: Missing[WebhookDeploymentStatusCreatedPropWorkflowRunPropRepository] = (
        Field(default=UNSET)
    )
    rerun_url: Missing[str] = Field(default=UNSET)
    run_attempt: int = Field()
    run_number: int = Field()
    run_started_at: datetime = Field()
    status: Literal[
        "requested", "in_progress", "completed", "queued", "waiting", "pending"
    ] = Field()
    triggering_actor: Union[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropTriggeringActor, None
    ] = Field(title="User")
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRunPropActor(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItems(
    GitHubModel
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str = Field()
    ref: Missing[str] = Field(default=UNSET)
    sha: str = Field()


class WebhookDeploymentStatusCreatedPropWorkflowRunPropTriggeringActor(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepository(GitHubModel):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepository"""

    archive_url: Missing[str] = Field(default=UNSET)
    assignees_url: Missing[str] = Field(default=UNSET)
    blobs_url: Missing[str] = Field(default=UNSET)
    branches_url: Missing[str] = Field(default=UNSET)
    collaborators_url: Missing[str] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    compare_url: Missing[str] = Field(default=UNSET)
    contents_url: Missing[str] = Field(default=UNSET)
    contributors_url: Missing[str] = Field(default=UNSET)
    deployments_url: Missing[str] = Field(default=UNSET)
    description: Missing[None] = Field(default=UNSET)
    downloads_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    fork: Missing[bool] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    full_name: Missing[str] = Field(default=UNSET)
    git_commits_url: Missing[str] = Field(default=UNSET)
    git_refs_url: Missing[str] = Field(default=UNSET)
    git_tags_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    issue_comment_url: Missing[str] = Field(default=UNSET)
    issue_events_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    keys_url: Missing[str] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    languages_url: Missing[str] = Field(default=UNSET)
    merges_url: Missing[str] = Field(default=UNSET)
    milestones_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    notifications_url: Missing[str] = Field(default=UNSET)
    owner: Missing[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwner
    ] = Field(default=UNSET)
    private: Missing[bool] = Field(default=UNSET)
    pulls_url: Missing[str] = Field(default=UNSET)
    releases_url: Missing[str] = Field(default=UNSET)
    stargazers_url: Missing[str] = Field(default=UNSET)
    statuses_url: Missing[str] = Field(default=UNSET)
    subscribers_url: Missing[str] = Field(default=UNSET)
    subscription_url: Missing[str] = Field(default=UNSET)
    tags_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)
    trees_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwner(
    GitHubModel
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwner"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRunPropRepository(GitHubModel):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropRepository"""

    archive_url: Missing[str] = Field(default=UNSET)
    assignees_url: Missing[str] = Field(default=UNSET)
    blobs_url: Missing[str] = Field(default=UNSET)
    branches_url: Missing[str] = Field(default=UNSET)
    collaborators_url: Missing[str] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    commits_url: Missing[str] = Field(default=UNSET)
    compare_url: Missing[str] = Field(default=UNSET)
    contents_url: Missing[str] = Field(default=UNSET)
    contributors_url: Missing[str] = Field(default=UNSET)
    deployments_url: Missing[str] = Field(default=UNSET)
    description: Missing[None] = Field(default=UNSET)
    downloads_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    fork: Missing[bool] = Field(default=UNSET)
    forks_url: Missing[str] = Field(default=UNSET)
    full_name: Missing[str] = Field(default=UNSET)
    git_commits_url: Missing[str] = Field(default=UNSET)
    git_refs_url: Missing[str] = Field(default=UNSET)
    git_tags_url: Missing[str] = Field(default=UNSET)
    hooks_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    issue_comment_url: Missing[str] = Field(default=UNSET)
    issue_events_url: Missing[str] = Field(default=UNSET)
    issues_url: Missing[str] = Field(default=UNSET)
    keys_url: Missing[str] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    languages_url: Missing[str] = Field(default=UNSET)
    merges_url: Missing[str] = Field(default=UNSET)
    milestones_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    notifications_url: Missing[str] = Field(default=UNSET)
    owner: Missing[
        WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwner
    ] = Field(default=UNSET)
    private: Missing[bool] = Field(default=UNSET)
    pulls_url: Missing[str] = Field(default=UNSET)
    releases_url: Missing[str] = Field(default=UNSET)
    stargazers_url: Missing[str] = Field(default=UNSET)
    statuses_url: Missing[str] = Field(default=UNSET)
    subscribers_url: Missing[str] = Field(default=UNSET)
    subscription_url: Missing[str] = Field(default=UNSET)
    tags_url: Missing[str] = Field(default=UNSET)
    teams_url: Missing[str] = Field(default=UNSET)
    trees_url: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwner(GitHubModel):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwner"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItems(GitHubModel):
    """Check Run Pull Request"""

    base: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBase = (
        Field()
    )
    head: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHead = (
        Field()
    )
    id: int = Field()
    number: int = Field()
    url: str = Field()


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBase(
    GitHubModel
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHead(
    GitHubModel
):
    """WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(WebhookDeploymentStatusCreated)
model_rebuild(WebhookDeploymentStatusCreatedPropCheckRun)
model_rebuild(WebhookDeploymentStatusCreatedPropDeployment)
model_rebuild(WebhookDeploymentStatusCreatedPropDeploymentPropCreator)
model_rebuild(WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1)
model_rebuild(WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubApp)
model_rebuild(
    WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropOwner
)
model_rebuild(
    WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions
)
model_rebuild(WebhookDeploymentStatusCreatedPropDeploymentStatus)
model_rebuild(WebhookDeploymentStatusCreatedPropDeploymentStatusPropCreator)
model_rebuild(
    WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubApp
)
model_rebuild(
    WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropOwner
)
model_rebuild(
    WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropPermissions
)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRun)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropActor)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItems)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropTriggeringActor)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepository)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwner)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropRepository)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwner)
model_rebuild(WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItems)
model_rebuild(
    WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBase
)
model_rebuild(
    WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo
)
model_rebuild(
    WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHead
)
model_rebuild(
    WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookDeploymentStatusCreated",
    "WebhookDeploymentStatusCreatedPropCheckRun",
    "WebhookDeploymentStatusCreatedPropDeployment",
    "WebhookDeploymentStatusCreatedPropDeploymentPropCreator",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPayloadOneof1",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubApp",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropOwner",
    "WebhookDeploymentStatusCreatedPropDeploymentPropPerformedViaGithubAppPropPermissions",
    "WebhookDeploymentStatusCreatedPropDeploymentStatus",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropCreator",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubApp",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropOwner",
    "WebhookDeploymentStatusCreatedPropDeploymentStatusPropPerformedViaGithubAppPropPermissions",
    "WebhookDeploymentStatusCreatedPropWorkflowRun",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropActor",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepository",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropHeadRepositoryPropOwner",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItems",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBase",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHead",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropReferencedWorkflowsItems",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropRepository",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropRepositoryPropOwner",
    "WebhookDeploymentStatusCreatedPropWorkflowRunPropTriggeringActor",
)
