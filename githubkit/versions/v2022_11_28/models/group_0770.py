"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0028 import CopilotSeatDetails


class EnterprisesEnterpriseCopilotBillingSeatsGetResponse200(GitHubModel):
    """EnterprisesEnterpriseCopilotBillingSeatsGetResponse200"""

    total_seats: Missing[int] = Field(
        default=UNSET,
        description="The total number of Copilot seats the enterprise is being billed for. Users with access through multiple organizations or enterprise teams are only counted once.",
    )
    seats: Missing[List[CopilotSeatDetails]] = Field(default=UNSET)


model_rebuild(EnterprisesEnterpriseCopilotBillingSeatsGetResponse200)

__all__ = ("EnterprisesEnterpriseCopilotBillingSeatsGetResponse200",)
