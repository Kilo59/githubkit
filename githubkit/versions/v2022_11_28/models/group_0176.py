"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0027 import Team
from .group_0001 import SimpleUser


class PendingDeploymentPropReviewersItems(GitHubModel):
    """PendingDeploymentPropReviewersItems"""

    type: Missing[Literal["User", "Team"]] = Field(
        default=UNSET, description="The type of reviewer."
    )
    reviewer: Missing[Union[SimpleUser, Team]] = Field(default=UNSET)


class PendingDeployment(GitHubModel):
    """Pending Deployment

    Details of a deployment that is waiting for protection rules to pass
    """

    environment: PendingDeploymentPropEnvironment = Field()
    wait_timer: int = Field(description="The set duration of the wait timer")
    wait_timer_started_at: Union[datetime, None] = Field(
        description="The time that the wait timer began."
    )
    current_user_can_approve: bool = Field(
        description="Whether the currently authenticated user can approve the deployment"
    )
    reviewers: List[PendingDeploymentPropReviewersItems] = Field(
        description="The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed."
    )


class PendingDeploymentPropEnvironment(GitHubModel):
    """PendingDeploymentPropEnvironment"""

    id: Missing[int] = Field(default=UNSET, description="The id of the environment.")
    node_id: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(
        default=UNSET, description="The name of the environment."
    )
    url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)


model_rebuild(PendingDeploymentPropReviewersItems)
model_rebuild(PendingDeployment)
model_rebuild(PendingDeploymentPropEnvironment)

__all__ = (
    "PendingDeploymentPropReviewersItems",
    "PendingDeployment",
    "PendingDeploymentPropEnvironment",
)
