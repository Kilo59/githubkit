"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoActionsWorkflowsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsWorkflowsGetResponse200"""

    total_count: int
    workflows: list[WorkflowType]


class WorkflowType(TypedDict):
    """Workflow

    A GitHub Actions workflow
    """

    id: int
    node_id: str
    name: str
    path: str
    state: Literal[
        "active", "deleted", "disabled_fork", "disabled_inactivity", "disabled_manually"
    ]
    created_at: datetime
    updated_at: datetime
    url: str
    html_url: str
    badge_url: str
    deleted_at: NotRequired[datetime]


__all__ = (
    "ReposOwnerRepoActionsWorkflowsGetResponse200Type",
    "WorkflowType",
)
