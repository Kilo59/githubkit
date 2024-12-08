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


class RepositoryRuleCodeScanning(GitHubModel):
    """code_scanning

    Choose which tools must provide code scanning results before the reference is
    updated. When configured, code scanning must be enabled and have results for
    both the commit and the reference being updated.
    """

    type: Literal["code_scanning"] = Field()
    parameters: Missing[RepositoryRuleCodeScanningPropParameters] = Field(default=UNSET)


model_rebuild(RepositoryRuleCodeScanning)

__all__ = ("RepositoryRuleCodeScanning",)
