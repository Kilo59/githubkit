"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType(TypedDict):
    """ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody"""

    state: Literal["open", "dismissed"]
    dismissed_reason: NotRequired[
        Union[None, Literal["false positive", "won't fix", "used in tests"]]
    ]
    dismissed_comment: NotRequired[Union[str, None]]
    create_request: NotRequired[bool]


__all__ = ("ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType",)
