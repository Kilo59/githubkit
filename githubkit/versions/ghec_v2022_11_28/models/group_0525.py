"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0427 import EnterpriseWebhooks
from .group_0428 import SimpleInstallation
from .group_0430 import RepositoryWebhooks
from .group_0439 import WebhooksWorkflowJobRun
from .group_0429 import OrganizationSimpleWebhooks
from .group_0438 import WebhooksApprover, WebhooksReviewersItems


class WebhookDeploymentReviewApproved(GitHubModel):
    """WebhookDeploymentReviewApproved"""

    action: Literal["approved"] = Field()
    approver: Missing[WebhooksApprover] = Field(default=UNSET)
    comment: Missing[str] = Field(default=UNSET)
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    reviewers: Missing[list[WebhooksReviewersItems]] = Field(default=UNSET)
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    since: str = Field()
    workflow_job_run: Missing[WebhooksWorkflowJobRun] = Field(default=UNSET)
    workflow_job_runs: Missing[
        list[WebhookDeploymentReviewApprovedPropWorkflowJobRunsItems]
    ] = Field(default=UNSET)
    workflow_run: Union[WebhookDeploymentReviewApprovedPropWorkflowRun, None] = Field(
        title="Deployment Workflow Run"
    )


class WebhookDeploymentReviewApprovedPropWorkflowJobRunsItems(GitHubModel):
    """WebhookDeploymentReviewApprovedPropWorkflowJobRunsItems"""

    conclusion: Missing[None] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    environment: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    name: Missing[Union[str, None]] = Field(default=UNSET)
    status: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)


class WebhookDeploymentReviewApprovedPropWorkflowRun(GitHubModel):
    """Deployment Workflow Run"""

    actor: Union[WebhookDeploymentReviewApprovedPropWorkflowRunPropActor, None] = Field(
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
        ],
    ] = Field()
    created_at: datetime = Field()
    display_title: str = Field()
    event: str = Field()
    head_branch: str = Field()
    head_commit: Missing[
        Union[WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommit, None]
    ] = Field(default=UNSET)
    head_repository: Missing[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepository
    ] = Field(default=UNSET)
    head_sha: str = Field()
    html_url: str = Field()
    id: int = Field()
    jobs_url: Missing[str] = Field(default=UNSET)
    logs_url: Missing[str] = Field(default=UNSET)
    name: str = Field()
    node_id: str = Field()
    path: str = Field()
    previous_attempt_url: Missing[Union[str, None]] = Field(default=UNSET)
    pull_requests: list[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItems
    ] = Field()
    referenced_workflows: Missing[
        Union[
            list[
                WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItems
            ],
            None,
        ]
    ] = Field(default=UNSET)
    repository: Missing[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropRepository
    ] = Field(default=UNSET)
    rerun_url: Missing[str] = Field(default=UNSET)
    run_attempt: int = Field()
    run_number: int = Field()
    run_started_at: datetime = Field()
    status: Literal[
        "requested", "in_progress", "completed", "queued", "waiting", "pending"
    ] = Field()
    triggering_actor: Union[
        WebhookDeploymentReviewApprovedPropWorkflowRunPropTriggeringActor, None
    ] = Field(title="User")
    updated_at: datetime = Field()
    url: str = Field()
    workflow_id: int = Field()
    workflow_url: Missing[str] = Field(default=UNSET)


class WebhookDeploymentReviewApprovedPropWorkflowRunPropActor(GitHubModel):
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


class WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommit(GitHubModel):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommit"""


class WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItems(
    GitHubModel
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItems"""

    path: str = Field()
    ref: Missing[str] = Field(default=UNSET)
    sha: str = Field()


class WebhookDeploymentReviewApprovedPropWorkflowRunPropTriggeringActor(GitHubModel):
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


class WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepository(GitHubModel):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepository"""

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
    description: Missing[Union[str, None]] = Field(default=UNSET)
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
        WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwner
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


class WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwner(
    GitHubModel
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwner"""

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
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentReviewApprovedPropWorkflowRunPropRepository(GitHubModel):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropRepository"""

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
    description: Missing[Union[str, None]] = Field(default=UNSET)
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
        WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwner
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


class WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwner(
    GitHubModel
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwner"""

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
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItems(GitHubModel):
    """Check Run Pull Request"""

    base: WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBase = Field()
    head: WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHead = Field()
    id: int = Field()
    number: int = Field()
    url: str = Field()


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBase(
    GitHubModel
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBase"""

    ref: str = Field()
    repo: WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHead(
    GitHubModel
):
    """WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHead"""

    ref: str = Field()
    repo: WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo = Field(
        title="Repo Ref"
    )
    sha: str = Field()


class WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo(
    GitHubModel
):
    """Repo Ref"""

    id: int = Field()
    name: str = Field()
    url: str = Field()


model_rebuild(WebhookDeploymentReviewApproved)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowJobRunsItems)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRun)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropActor)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommit)
model_rebuild(
    WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItems
)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropTriggeringActor)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepository)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwner)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropRepository)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwner)
model_rebuild(WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItems)
model_rebuild(
    WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBase
)
model_rebuild(
    WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo
)
model_rebuild(
    WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHead
)
model_rebuild(
    WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo
)

__all__ = (
    "WebhookDeploymentReviewApproved",
    "WebhookDeploymentReviewApprovedPropWorkflowJobRunsItems",
    "WebhookDeploymentReviewApprovedPropWorkflowRun",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropActor",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadCommit",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropReferencedWorkflowsItems",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropTriggeringActor",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepository",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropHeadRepositoryPropOwner",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropRepository",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropRepositoryPropOwner",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItems",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBase",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropBasePropRepo",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHead",
    "WebhookDeploymentReviewApprovedPropWorkflowRunPropPullRequestsItemsPropHeadPropRepo",
)
