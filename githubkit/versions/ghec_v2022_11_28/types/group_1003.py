"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0205 import ActionsSecretType


class ReposOwnerRepoActionsSecretsGetResponse200Type(TypedDict):
    """ReposOwnerRepoActionsSecretsGetResponse200"""

    total_count: int
    secrets: list[ActionsSecretType]


__all__ = ("ReposOwnerRepoActionsSecretsGetResponse200Type",)
