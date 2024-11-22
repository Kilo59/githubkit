"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgActionsRunnerGroupsPostBodyType(TypedDict):
    """OrgsOrgActionsRunnerGroupsPostBody"""

    name: str
    visibility: NotRequired[Literal["selected", "all", "private"]]
    selected_repository_ids: NotRequired[list[int]]
    runners: NotRequired[list[int]]
    allows_public_repositories: NotRequired[bool]
    restricted_to_workflows: NotRequired[bool]
    selected_workflows: NotRequired[list[str]]


__all__ = ("OrgsOrgActionsRunnerGroupsPostBodyType",)
