"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType
from .group_0043 import SimpleRepositoryType
from .group_0234 import CodeScanningVariantAnalysisPropSkippedRepositoriesType
from .group_0233 import CodeScanningVariantAnalysisPropScannedRepositoriesItemsType


class CodeScanningVariantAnalysisType(TypedDict):
    """Variant Analysis

    A run of a CodeQL query against one or more repositories.
    """

    id: int
    controller_repo: SimpleRepositoryType
    actor: SimpleUserType
    query_language: Literal[
        "cpp", "csharp", "go", "java", "javascript", "python", "ruby", "swift"
    ]
    query_pack_url: str
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]
    completed_at: NotRequired[Union[datetime, None]]
    status: Literal["in_progress", "succeeded", "failed", "cancelled"]
    actions_workflow_run_id: NotRequired[int]
    failure_reason: NotRequired[
        Literal["no_repos_queried", "actions_workflow_run_failed", "internal_error"]
    ]
    scanned_repositories: NotRequired[
        List[CodeScanningVariantAnalysisPropScannedRepositoriesItemsType]
    ]
    skipped_repositories: NotRequired[
        CodeScanningVariantAnalysisPropSkippedRepositoriesType
    ]


__all__ = ("CodeScanningVariantAnalysisType",)
