"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0011 import WebhookConfigType


class ReposOwnerRepoHooksHookIdPatchBodyType(TypedDict):
    """ReposOwnerRepoHooksHookIdPatchBody"""

    config: NotRequired[WebhookConfigType]
    events: NotRequired[list[str]]
    add_events: NotRequired[list[str]]
    remove_events: NotRequired[list[str]]
    active: NotRequired[bool]


__all__ = ("ReposOwnerRepoHooksHookIdPatchBodyType",)
