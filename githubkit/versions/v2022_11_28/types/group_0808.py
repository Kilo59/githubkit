"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0052 import MinimalRepositoryType


class OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesGetResponse200Type(TypedDict):
    """OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesGetResponse200"""

    total_count: float
    repositories: list[MinimalRepositoryType]


__all__ = ("OrgsOrgActionsRunnerGroupsRunnerGroupIdRepositoriesGetResponse200Type",)
