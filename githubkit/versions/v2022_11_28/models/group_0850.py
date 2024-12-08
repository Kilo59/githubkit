"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class OrgsOrgCopilotBillingSelectedUsersDeleteResponse200(GitHubModel):
    """OrgsOrgCopilotBillingSelectedUsersDeleteResponse200

    The total number of seats set to "pending cancellation" for the specified users.
    """

    seats_cancelled: int = Field()


model_rebuild(OrgsOrgCopilotBillingSelectedUsersDeleteResponse200)

__all__ = ("OrgsOrgCopilotBillingSelectedUsersDeleteResponse200",)
