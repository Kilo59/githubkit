"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import TypedDict


class RepositorySubscriptionType(TypedDict):
    """Repository Invitation

    Repository invitations let you manage who you collaborate with.
    """

    subscribed: bool
    ignored: bool
    reason: Union[str, None]
    created_at: datetime
    url: str
    repository_url: str


__all__ = ("RepositorySubscriptionType",)
