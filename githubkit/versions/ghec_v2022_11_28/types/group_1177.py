"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoMilestonesPostBodyType(TypedDict):
    """ReposOwnerRepoMilestonesPostBody"""

    title: str
    state: NotRequired[Literal["open", "closed"]]
    description: NotRequired[str]
    due_on: NotRequired[datetime]


__all__ = ("ReposOwnerRepoMilestonesPostBodyType",)
