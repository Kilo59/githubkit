"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class RepositoryRulesetBypassActorType(TypedDict):
    """Repository Ruleset Bypass Actor

    An actor that can bypass rules in a ruleset
    """

    actor_id: NotRequired[Union[int, None]]
    actor_type: Literal[
        "Integration", "OrganizationAdmin", "RepositoryRole", "Team", "DeployKey"
    ]
    bypass_mode: NotRequired[Literal["always", "pull_request"]]


__all__ = ("RepositoryRulesetBypassActorType",)
