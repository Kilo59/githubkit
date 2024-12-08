"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import PYDANTIC_V2, GitHubModel, model_rebuild

from .group_0137 import CustomPropertyValue


class OrgsOrgPropertiesValuesPatchBody(GitHubModel):
    """OrgsOrgPropertiesValuesPatchBody"""

    repository_names: list[str] = Field(
        max_length=30 if PYDANTIC_V2 else None,
        min_length=1 if PYDANTIC_V2 else None,
        description="The names of repositories that the custom property values will be applied to.",
    )
    properties: list[CustomPropertyValue] = Field(
        description="List of custom property names and associated values to apply to the repositories."
    )


model_rebuild(OrgsOrgPropertiesValuesPatchBody)

__all__ = ("OrgsOrgPropertiesValuesPatchBody",)
