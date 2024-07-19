"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof0(GitHubModel):
    """ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof0"""

    language: Literal[
        "cpp", "csharp", "go", "java", "javascript", "python", "ruby", "swift"
    ] = Field(description="The language targeted by the CodeQL query")
    query_pack: str = Field(
        description="A Base64-encoded tarball containing a CodeQL query and all its dependencies"
    )
    repositories: List[str] = Field(
        description="List of repository names (in the form `owner/repo-name`) to run the query against. Precisely one property from `repositories`, `repository_lists` and `repository_owners` is required."
    )
    repository_lists: Missing[List[str]] = Field(
        max_length=1,
        default=UNSET,
        description="List of repository lists to run the query against. Precisely one property from `repositories`, `repository_lists` and `repository_owners` is required.",
    )
    repository_owners: Missing[List[str]] = Field(
        max_length=1,
        default=UNSET,
        description="List of organization or user names whose repositories the query should be run against. Precisely one property from `repositories`, `repository_lists` and `repository_owners` is required.",
    )


model_rebuild(ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof0)

__all__ = ("ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof0",)
