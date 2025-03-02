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


class Job(GitHubModel):
    """Job

    Information of a job execution in a workflow run
    """

    id: int = Field(description="The id of the job.")
    run_id: int = Field(description="The id of the associated workflow run.")
    run_url: str = Field()
    run_attempt: Missing[int] = Field(
        default=UNSET,
        description="Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run.",
    )
    node_id: str = Field()
    head_sha: str = Field(description="The SHA of the commit that is being run.")
    url: str = Field()
    html_url: Union[str, None] = Field()
    status: Literal[
        "queued", "in_progress", "completed", "waiting", "requested", "pending"
    ] = Field(description="The phase of the lifecycle that the job is currently in.")
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
        ],
    ] = Field(description="The outcome of the job.")
    created_at: datetime = Field(
        description="The time that the job created, in ISO 8601 format."
    )
    started_at: datetime = Field(
        description="The time that the job started, in ISO 8601 format."
    )
    completed_at: Union[datetime, None] = Field(
        description="The time that the job finished, in ISO 8601 format."
    )
    name: str = Field(description="The name of the job.")
    steps: Missing[list[JobPropStepsItems]] = Field(
        default=UNSET, description="Steps in this job."
    )
    check_run_url: str = Field()
    labels: list[str] = Field(
        description='Labels for the workflow job. Specified by the "runs_on" attribute in the action\'s workflow file.'
    )
    runner_id: Union[int, None] = Field(
        description="The ID of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)"
    )
    runner_name: Union[str, None] = Field(
        description="The name of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)"
    )
    runner_group_id: Union[int, None] = Field(
        description="The ID of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)"
    )
    runner_group_name: Union[str, None] = Field(
        description="The name of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)"
    )
    workflow_name: Union[str, None] = Field(description="The name of the workflow.")
    head_branch: Union[str, None] = Field(description="The name of the current branch.")


class JobPropStepsItems(GitHubModel):
    """JobPropStepsItems"""

    status: Literal["queued", "in_progress", "completed"] = Field(
        description="The phase of the lifecycle that the job is currently in."
    )
    conclusion: Union[str, None] = Field(description="The outcome of the job.")
    name: str = Field(description="The name of the job.")
    number: int = Field()
    started_at: Missing[Union[datetime, None]] = Field(
        default=UNSET, description="The time that the step started, in ISO 8601 format."
    )
    completed_at: Missing[Union[datetime, None]] = Field(
        default=UNSET, description="The time that the job finished, in ISO 8601 format."
    )


model_rebuild(Job)
model_rebuild(JobPropStepsItems)

__all__ = (
    "Job",
    "JobPropStepsItems",
)
