"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof2Type(TypedDict):
    """ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof2"""

    labels: NotRequired[
        list[ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof2PropLabelsItemsType]
    ]


class ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof2PropLabelsItemsType(TypedDict):
    """ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof2PropLabelsItems"""

    name: str


__all__ = (
    "ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof2Type",
    "ReposOwnerRepoIssuesIssueNumberLabelsPostBodyOneof2PropLabelsItemsType",
)
