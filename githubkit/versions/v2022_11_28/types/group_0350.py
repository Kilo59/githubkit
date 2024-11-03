"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType


class ContributorActivityType(TypedDict):
    """Contributor Activity

    Contributor Activity
    """

    author: Union[None, SimpleUserType]
    total: int
    weeks: list[ContributorActivityPropWeeksItemsType]


class ContributorActivityPropWeeksItemsType(TypedDict):
    """ContributorActivityPropWeeksItems"""

    w: NotRequired[int]
    a: NotRequired[int]
    d: NotRequired[int]
    c: NotRequired[int]


__all__ = (
    "ContributorActivityType",
    "ContributorActivityPropWeeksItemsType",
)
