"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict


class CodeScanningVariantAnalysisRepositoryType(TypedDict):
    """Repository Identifier

    Repository Identifier
    """

    id: int
    name: str
    full_name: str
    private: bool
    stargazers_count: int
    updated_at: Union[datetime, None]


__all__ = ("CodeScanningVariantAnalysisRepositoryType",)
