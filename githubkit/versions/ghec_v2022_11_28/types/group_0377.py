"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class GroupResponseType(TypedDict):
    """GroupResponse"""

    schemas: List[
        Literal[
            "urn:ietf:params:scim:schemas:core:2.0:Group",
            "urn:ietf:params:scim:api:messages:2.0:ListResponse",
        ]
    ]
    external_id: NotRequired[Union[str, None]]
    display_name: NotRequired[Union[str, None]]
    members: NotRequired[List[GroupResponsePropMembersItemsType]]


class GroupResponsePropMembersItemsType(TypedDict):
    """GroupResponsePropMembersItems"""

    value: str
    ref: str
    display: NotRequired[str]


__all__ = (
    "GroupResponseType",
    "GroupResponsePropMembersItemsType",
)
