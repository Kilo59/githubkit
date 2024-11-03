"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0105 import CustomPropertyValue


class OrgRepoCustomPropertyValues(GitHubModel):
    """Organization Repository Custom Property Values

    List of custom property values for a repository
    """

    repository_id: int = Field()
    repository_name: str = Field()
    repository_full_name: str = Field()
    properties: list[CustomPropertyValue] = Field(
        description="List of custom property names and associated values"
    )


model_rebuild(OrgRepoCustomPropertyValues)

__all__ = ("OrgRepoCustomPropertyValues",)
