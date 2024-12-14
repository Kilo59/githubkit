"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ActionsVariable(GitHubModel):
    """Actions Variable"""

    name: str = Field(description="The name of the variable.")
    value: str = Field(description="The value of the variable.")
    created_at: datetime = Field(
        description="The date and time at which the variable was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    updated_at: datetime = Field(
        description="The date and time at which the variable was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )


model_rebuild(ActionsVariable)

__all__ = ("ActionsVariable",)
