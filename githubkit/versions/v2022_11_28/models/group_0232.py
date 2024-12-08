"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0058 import MinimalRepository


class RepositoryInvitation(GitHubModel):
    """Repository Invitation

    Repository invitations let you manage who you collaborate with.
    """

    id: int = Field(description="Unique identifier of the repository invitation.")
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    invitee: Union[None, SimpleUser] = Field()
    inviter: Union[None, SimpleUser] = Field()
    permissions: Literal["read", "write", "admin", "triage", "maintain"] = Field(
        description="The permission associated with the invitation."
    )
    created_at: datetime = Field()
    expired: Missing[bool] = Field(
        default=UNSET, description="Whether or not the invitation has expired"
    )
    url: str = Field(description="URL for the repository invitation")
    html_url: str = Field()
    node_id: str = Field()


model_rebuild(RepositoryInvitation)

__all__ = ("RepositoryInvitation",)
