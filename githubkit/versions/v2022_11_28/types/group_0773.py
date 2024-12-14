"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0189 import DeploymentType
from .group_0389 import EnterpriseWebhooksType
from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0392 import RepositoryWebhooksType


class WebhookWorkflowJobWaitingType(TypedDict):
    """workflow_job waiting event"""

    action: Literal["waiting"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType
    workflow_job: WebhookWorkflowJobWaitingPropWorkflowJobType
    deployment: NotRequired[DeploymentType]


class WebhookWorkflowJobWaitingPropWorkflowJobType(TypedDict):
    """WebhookWorkflowJobWaitingPropWorkflowJob"""

    check_run_url: str
    completed_at: Union[str, None]
    conclusion: Union[str, None]
    created_at: str
    head_sha: str
    html_url: str
    id: int
    labels: list[str]
    name: str
    node_id: str
    run_attempt: int
    run_id: int
    run_url: str
    runner_group_id: Union[int, None]
    runner_group_name: Union[str, None]
    runner_id: Union[int, None]
    runner_name: Union[str, None]
    started_at: datetime
    head_branch: Union[str, None]
    workflow_name: Union[str, None]
    status: Literal["queued", "in_progress", "completed", "waiting"]
    steps: list[WebhookWorkflowJobWaitingPropWorkflowJobPropStepsItemsType]
    url: str


class WebhookWorkflowJobWaitingPropWorkflowJobPropStepsItemsType(TypedDict):
    """Workflow Step"""

    completed_at: Union[str, None]
    conclusion: Union[None, Literal["failure", "skipped", "success", "cancelled"]]
    name: str
    number: int
    started_at: Union[str, None]
    status: Literal["completed", "in_progress", "queued", "pending", "waiting"]


__all__ = (
    "WebhookWorkflowJobWaitingPropWorkflowJobPropStepsItemsType",
    "WebhookWorkflowJobWaitingPropWorkflowJobType",
    "WebhookWorkflowJobWaitingType",
)
