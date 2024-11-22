"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0051 import SimpleRepository


class CodeSecurityConfigurationRepositories(GitHubModel):
    """CodeSecurityConfigurationRepositories

    Repositories associated with a code security configuration and attachment status
    """

    status: Missing[
        Literal[
            "attached",
            "attaching",
            "detached",
            "removed",
            "enforced",
            "failed",
            "updating",
            "removed_by_enterprise",
        ]
    ] = Field(
        default=UNSET,
        description="The attachment status of the code security configuration on the repository.",
    )
    repository: Missing[SimpleRepository] = Field(
        default=UNSET, title="Simple Repository", description="A GitHub repository."
    )


model_rebuild(CodeSecurityConfigurationRepositories)

__all__ = ("CodeSecurityConfigurationRepositories",)
