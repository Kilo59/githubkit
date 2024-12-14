"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0143 import MinimalRepositoryType


class RepositoryInvitationType(TypedDict):
    """Repository Invitation

    Repository invitations let you manage who you collaborate with.
    """

    id: int
    repository: MinimalRepositoryType
    invitee: Union[None, SimpleUserType]
    inviter: Union[None, SimpleUserType]
    permissions: Literal["read", "write", "admin", "triage", "maintain"]
    created_at: datetime
    expired: NotRequired[bool]
    url: str
    html_url: str
    node_id: str


__all__ = ("RepositoryInvitationType",)
