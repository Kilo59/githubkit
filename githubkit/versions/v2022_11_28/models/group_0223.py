"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0220 import CodeScanningVariantAnalysisSkippedRepoGroup


class CodeScanningVariantAnalysisPropSkippedRepositories(GitHubModel):
    """CodeScanningVariantAnalysisPropSkippedRepositories

    Information about repositories that were skipped from processing. This
    information is only available to the user that initiated the variant analysis.
    """

    access_mismatch_repos: CodeScanningVariantAnalysisSkippedRepoGroup = Field()
    not_found_repos: CodeScanningVariantAnalysisPropSkippedRepositoriesPropNotFoundRepos = Field()
    no_codeql_db_repos: CodeScanningVariantAnalysisSkippedRepoGroup = Field()
    over_limit_repos: CodeScanningVariantAnalysisSkippedRepoGroup = Field()


class CodeScanningVariantAnalysisPropSkippedRepositoriesPropNotFoundRepos(GitHubModel):
    """CodeScanningVariantAnalysisPropSkippedRepositoriesPropNotFoundRepos"""

    repository_count: int = Field(
        description="The total number of repositories that were skipped for this reason."
    )
    repository_full_names: list[str] = Field(
        description="A list of full repository names that were skipped. This list may not include all repositories that were skipped."
    )


model_rebuild(CodeScanningVariantAnalysisPropSkippedRepositories)
model_rebuild(CodeScanningVariantAnalysisPropSkippedRepositoriesPropNotFoundRepos)

__all__ = (
    "CodeScanningVariantAnalysisPropSkippedRepositories",
    "CodeScanningVariantAnalysisPropSkippedRepositoriesPropNotFoundRepos",
)
