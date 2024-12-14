"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoIssuesIssueNumberPatchBodyType(TypedDict):
    """ReposOwnerRepoIssuesIssueNumberPatchBody"""

    title: NotRequired[Union[str, int, None]]
    body: NotRequired[Union[str, None]]
    assignee: NotRequired[Union[str, None]]
    state: NotRequired[Literal["open", "closed"]]
    state_reason: NotRequired[
        Union[None, Literal["completed", "not_planned", "reopened"]]
    ]
    milestone: NotRequired[Union[str, int, None]]
    labels: NotRequired[
        list[
            Union[
                str, ReposOwnerRepoIssuesIssueNumberPatchBodyPropLabelsItemsOneof1Type
            ]
        ]
    ]
    assignees: NotRequired[list[str]]


class ReposOwnerRepoIssuesIssueNumberPatchBodyPropLabelsItemsOneof1Type(TypedDict):
    """ReposOwnerRepoIssuesIssueNumberPatchBodyPropLabelsItemsOneof1"""

    id: NotRequired[int]
    name: NotRequired[str]
    description: NotRequired[Union[str, None]]
    color: NotRequired[Union[str, None]]


__all__ = (
    "ReposOwnerRepoIssuesIssueNumberPatchBodyPropLabelsItemsOneof1Type",
    "ReposOwnerRepoIssuesIssueNumberPatchBodyType",
)
