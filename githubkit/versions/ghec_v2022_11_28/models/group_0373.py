"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0180 import RepositoryRuleCodeScanningPropParameters


class RepositoryRuleDetailedOneof16(GitHubModel):
    """RepositoryRuleDetailedOneof16"""

    type: Literal["code_scanning"] = Field()
    parameters: Missing[RepositoryRuleCodeScanningPropParameters] = Field(default=UNSET)
    ruleset_source_type: Missing[Literal["Repository", "Organization"]] = Field(
        default=UNSET,
        description="The type of source for the ruleset that includes this rule.",
    )
    ruleset_source: Missing[str] = Field(
        default=UNSET,
        description="The name of the source of the ruleset that includes this rule.",
    )
    ruleset_id: Missing[int] = Field(
        default=UNSET, description="The ID of the ruleset that includes this rule."
    )


model_rebuild(RepositoryRuleDetailedOneof16)

__all__ = ("RepositoryRuleDetailedOneof16",)
