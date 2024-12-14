"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class UserCodespacesSecretsGetResponse200(GitHubModel):
    """UserCodespacesSecretsGetResponse200"""

    total_count: int = Field()
    secrets: list[CodespacesSecret] = Field()


class CodespacesSecret(GitHubModel):
    """Codespaces Secret

    Secrets for a GitHub Codespace.
    """

    name: str = Field(description="The name of the secret")
    created_at: datetime = Field(
        description="The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    updated_at: datetime = Field(
        description="The date and time at which the secret was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ."
    )
    visibility: Literal["all", "private", "selected"] = Field(
        description="The type of repositories in the organization that the secret is visible to"
    )
    selected_repositories_url: str = Field(
        description="The API URL at which the list of repositories this secret is visible to can be retrieved"
    )


model_rebuild(UserCodespacesSecretsGetResponse200)
model_rebuild(CodespacesSecret)

__all__ = (
    "CodespacesSecret",
    "UserCodespacesSecretsGetResponse200",
)
