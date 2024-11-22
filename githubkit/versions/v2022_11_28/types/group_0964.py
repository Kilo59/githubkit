"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoCodespacesDevcontainersGetResponse200Type(TypedDict):
    """ReposOwnerRepoCodespacesDevcontainersGetResponse200"""

    total_count: int
    devcontainers: list[
        ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItemsType
    ]


class ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItemsType(
    TypedDict
):
    """ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItems"""

    path: str
    name: NotRequired[str]
    display_name: NotRequired[str]


__all__ = (
    "ReposOwnerRepoCodespacesDevcontainersGetResponse200Type",
    "ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItemsType",
)
