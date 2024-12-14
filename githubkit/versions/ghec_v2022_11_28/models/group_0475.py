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

from .group_0002 import SimpleUser


class ProjectsV2(GitHubModel):
    """Projects v2 Project

    A projects v2 project
    """

    id: float = Field()
    node_id: str = Field()
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    creator: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    title: str = Field()
    description: Union[str, None] = Field()
    public: bool = Field()
    closed_at: Union[datetime, None] = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    number: int = Field()
    short_description: Union[str, None] = Field()
    deleted_at: Union[datetime, None] = Field()
    deleted_by: Union[None, SimpleUser] = Field()


model_rebuild(ProjectsV2)

__all__ = ("ProjectsV2",)
