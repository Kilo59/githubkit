"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0003 import SimpleUser


class Status(GitHubModel):
    """Status

    The status of a commit.
    """

    url: str = Field()
    avatar_url: Union[str, None] = Field()
    id: int = Field()
    node_id: str = Field()
    state: str = Field()
    description: Union[str, None] = Field()
    target_url: Union[str, None] = Field()
    context: str = Field()
    created_at: str = Field()
    updated_at: str = Field()
    creator: Union[None, SimpleUser] = Field()


model_rebuild(Status)

__all__ = ("Status",)
