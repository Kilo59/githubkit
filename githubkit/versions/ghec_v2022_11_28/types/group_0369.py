"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0171 import RepositoryRuleCommitterEmailPatternPropParametersType


class RepositoryRuleDetailedOneof12Type(TypedDict):
    """RepositoryRuleDetailedOneof12"""

    type: Literal["committer_email_pattern"]
    parameters: NotRequired[RepositoryRuleCommitterEmailPatternPropParametersType]
    ruleset_source_type: NotRequired[Literal["Repository", "Organization"]]
    ruleset_source: NotRequired[str]
    ruleset_id: NotRequired[int]


__all__ = ("RepositoryRuleDetailedOneof12Type",)
