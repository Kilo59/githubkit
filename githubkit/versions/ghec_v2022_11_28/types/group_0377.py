"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0099 import RepositoryRuleCommitAuthorEmailPatternPropParametersType


class RepositoryRuleDetailedOneof11Type(TypedDict):
    """RepositoryRuleDetailedOneof11"""

    type: Literal["commit_author_email_pattern"]
    parameters: NotRequired[RepositoryRuleCommitAuthorEmailPatternPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof11Type",)
