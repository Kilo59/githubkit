"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof0Type(TypedDict):
    """ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof0"""

    language: Literal[
        "cpp", "csharp", "go", "java", "javascript", "python", "ruby", "swift"
    ]
    query_pack: str
    repositories: list[str]
    repository_lists: NotRequired[list[str]]
    repository_owners: NotRequired[list[str]]


__all__ = ("ReposOwnerRepoCodeScanningCodeqlVariantAnalysesPostBodyOneof0Type",)
