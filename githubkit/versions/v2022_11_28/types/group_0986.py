"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoDeploymentsPostBodyType(TypedDict):
    """ReposOwnerRepoDeploymentsPostBody"""

    ref: str
    task: NotRequired[str]
    auto_merge: NotRequired[bool]
    required_contexts: NotRequired[list[str]]
    payload: NotRequired[
        Union[ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0Type, str]
    ]
    environment: NotRequired[str]
    description: NotRequired[Union[str, None]]
    transient_environment: NotRequired[bool]
    production_environment: NotRequired[bool]


class ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0Type(TypedDict):
    """ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0"""


__all__ = (
    "ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0Type",
    "ReposOwnerRepoDeploymentsPostBodyType",
)
