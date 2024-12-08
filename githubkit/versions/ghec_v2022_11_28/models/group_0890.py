"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild


class OrgsOrgActionsRunnersRunnerIdLabelsPostBody(GitHubModel):
    """OrgsOrgActionsRunnersRunnerIdLabelsPostBody"""

    labels: list[str] = Field(
        max_length=100 if PYDANTIC_V2 else None,
        min_length=1 if PYDANTIC_V2 else None,
        description="The names of the custom labels to add to the runner.",
    )


model_rebuild(OrgsOrgActionsRunnersRunnerIdLabelsPostBody)

__all__ = ("OrgsOrgActionsRunnersRunnerIdLabelsPostBody",)
