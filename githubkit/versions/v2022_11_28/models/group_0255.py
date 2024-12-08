"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class DependencyGraphDiffItems(GitHubModel):
    """DependencyGraphDiffItems"""

    change_type: Literal["added", "removed"] = Field()
    manifest: str = Field()
    ecosystem: str = Field()
    name: str = Field()
    version: str = Field()
    package_url: Union[str, None] = Field()
    license_: Union[str, None] = Field(alias="license")
    source_repository_url: Union[str, None] = Field()
    vulnerabilities: list[DependencyGraphDiffItemsPropVulnerabilitiesItems] = Field()
    scope: Literal["unknown", "runtime", "development"] = Field(
        description="Where the dependency is utilized. `development` means that the dependency is only utilized in the development environment. `runtime` means that the dependency is utilized at runtime and in the development environment."
    )


class DependencyGraphDiffItemsPropVulnerabilitiesItems(GitHubModel):
    """DependencyGraphDiffItemsPropVulnerabilitiesItems"""

    severity: str = Field()
    advisory_ghsa_id: str = Field()
    advisory_summary: str = Field()
    advisory_url: str = Field()


model_rebuild(DependencyGraphDiffItems)
model_rebuild(DependencyGraphDiffItemsPropVulnerabilitiesItems)

__all__ = (
    "DependencyGraphDiffItems",
    "DependencyGraphDiffItemsPropVulnerabilitiesItems",
)
