"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookWorkflowJobCompletedPropWorkflowJobAllof1(GitHubModel):
    """WebhookWorkflowJobCompletedPropWorkflowJobAllof1"""

    check_run_url: Missing[str] = Field(default=UNSET)
    completed_at: Missing[str] = Field(default=UNSET)
    conclusion: Literal[
        "success",
        "failure",
        "skipped",
        "cancelled",
        "action_required",
        "neutral",
        "timed_out",
    ] = Field()
    created_at: Missing[str] = Field(
        default=UNSET, description="The time that the job created."
    )
    head_sha: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    labels: Missing[list[Union[str, None]]] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    run_attempt: Missing[int] = Field(default=UNSET)
    run_id: Missing[int] = Field(default=UNSET)
    run_url: Missing[str] = Field(default=UNSET)
    runner_group_id: Missing[Union[int, None]] = Field(default=UNSET)
    runner_group_name: Missing[Union[str, None]] = Field(default=UNSET)
    runner_id: Missing[Union[int, None]] = Field(default=UNSET)
    runner_name: Missing[Union[str, None]] = Field(default=UNSET)
    started_at: Missing[str] = Field(default=UNSET)
    status: Missing[str] = Field(default=UNSET)
    head_branch: Missing[Union[str, None]] = Field(
        default=UNSET, description="The name of the current branch."
    )
    workflow_name: Missing[Union[str, None]] = Field(
        default=UNSET, description="The name of the workflow."
    )
    steps: Missing[
        list[
            Union[WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItems, None]
        ]
    ] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItems(GitHubModel):
    """WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItems"""


model_rebuild(WebhookWorkflowJobCompletedPropWorkflowJobAllof1)
model_rebuild(WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItems)

__all__ = (
    "WebhookWorkflowJobCompletedPropWorkflowJobAllof1",
    "WebhookWorkflowJobCompletedPropWorkflowJobAllof1PropStepsItems",
)
