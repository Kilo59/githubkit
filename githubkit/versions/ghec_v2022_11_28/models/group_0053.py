"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class BypassResponse(GitHubModel):
    """Bypass response

    A response made by a delegated bypasser to a bypass request.
    """

    id: Missing[int] = Field(
        default=UNSET, description="The ID of the response to the bypass request."
    )
    reviewer: Missing[BypassResponsePropReviewer] = Field(
        default=UNSET, description="The user who reviewed the bypass request."
    )
    status: Missing[Literal["approved", "denied", "dismissed"]] = Field(
        default=UNSET,
        description="The response status to the bypass request until dismissed.",
    )
    created_at: Missing[datetime] = Field(
        default=UNSET,
        description="The date and time the response to the bypass request was created.",
    )


class BypassResponsePropReviewer(GitHubModel):
    """BypassResponsePropReviewer

    The user who reviewed the bypass request.
    """

    actor_id: Missing[int] = Field(
        default=UNSET,
        description="The ID of the GitHub user who reviewed the bypass request.",
    )
    actor_name: Missing[str] = Field(
        default=UNSET,
        description="The name of the GitHub user who reviewed the bypass request.",
    )


model_rebuild(BypassResponse)
model_rebuild(BypassResponsePropReviewer)

__all__ = (
    "BypassResponse",
    "BypassResponsePropReviewer",
)
