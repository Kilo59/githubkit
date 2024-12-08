"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoActionsWorkflowsWorkflowIdDispatchesPostBodyType(TypedDict):
    """ReposOwnerRepoActionsWorkflowsWorkflowIdDispatchesPostBody"""

    ref: str
    inputs: NotRequired[
        ReposOwnerRepoActionsWorkflowsWorkflowIdDispatchesPostBodyPropInputsType
    ]


class ReposOwnerRepoActionsWorkflowsWorkflowIdDispatchesPostBodyPropInputsType(
    TypedDict
):
    """ReposOwnerRepoActionsWorkflowsWorkflowIdDispatchesPostBodyPropInputs

    Input keys and values configured in the workflow file. The maximum number of
    properties is 10. Any default properties configured in the workflow file will be
    used when `inputs` are omitted.
    """


__all__ = (
    "ReposOwnerRepoActionsWorkflowsWorkflowIdDispatchesPostBodyPropInputsType",
    "ReposOwnerRepoActionsWorkflowsWorkflowIdDispatchesPostBodyType",
)
