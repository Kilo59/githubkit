"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0143 import MinimalRepository


class CombinedCommitStatus(GitHubModel):
    """Combined Commit Status

    Combined Commit Status
    """

    state: str = Field()
    statuses: list[SimpleCommitStatus] = Field()
    sha: str = Field()
    total_count: int = Field()
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    commit_url: str = Field()
    url: str = Field()


class SimpleCommitStatus(GitHubModel):
    """Simple Commit Status"""

    description: Union[str, None] = Field()
    id: int = Field()
    node_id: str = Field()
    state: str = Field()
    context: str = Field()
    target_url: Union[str, None] = Field()
    required: Missing[Union[bool, None]] = Field(default=UNSET)
    avatar_url: Union[str, None] = Field()
    url: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


model_rebuild(CombinedCommitStatus)
model_rebuild(SimpleCommitStatus)

__all__ = (
    "CombinedCommitStatus",
    "SimpleCommitStatus",
)
