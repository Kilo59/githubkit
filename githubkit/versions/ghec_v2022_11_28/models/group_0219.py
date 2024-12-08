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

from .group_0002 import SimpleUser


class Activity(GitHubModel):
    """Activity

    Activity
    """

    id: int = Field()
    node_id: str = Field()
    before: str = Field(description="The SHA of the commit before the activity.")
    after: str = Field(description="The SHA of the commit after the activity.")
    ref: str = Field(
        description="The full Git reference, formatted as `refs/heads/<branch name>`."
    )
    timestamp: datetime = Field(description="The time when the activity occurred.")
    activity_type: Literal[
        "push",
        "force_push",
        "branch_deletion",
        "branch_creation",
        "pr_merge",
        "merge_queue_merge",
    ] = Field(description="The type of the activity that was performed.")
    actor: Union[None, SimpleUser] = Field()


model_rebuild(Activity)

__all__ = ("Activity",)
