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

from .group_0108 import RepositoryRuleRequiredStatusChecksPropParameters


class RepositoryRuleRequiredStatusChecks(GitHubModel):
    """required_status_checks

    Choose which status checks must pass before the ref is updated. When enabled,
    commits must first be pushed to another ref where the checks pass.
    """

    type: Literal["required_status_checks"] = Field()
    parameters: Missing[RepositoryRuleRequiredStatusChecksPropParameters] = Field(
        default=UNSET
    )


model_rebuild(RepositoryRuleRequiredStatusChecks)

__all__ = ("RepositoryRuleRequiredStatusChecks",)
