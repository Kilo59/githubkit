"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class EnterprisesEnterpriseActionsRunnerGroupsPostBodyType(TypedDict):
    """EnterprisesEnterpriseActionsRunnerGroupsPostBody"""

    name: str
    visibility: NotRequired[Literal["selected", "all"]]
    selected_organization_ids: NotRequired[list[int]]
    runners: NotRequired[list[int]]
    allows_public_repositories: NotRequired[bool]
    restricted_to_workflows: NotRequired[bool]
    selected_workflows: NotRequired[list[str]]


__all__ = ("EnterprisesEnterpriseActionsRunnerGroupsPostBodyType",)
