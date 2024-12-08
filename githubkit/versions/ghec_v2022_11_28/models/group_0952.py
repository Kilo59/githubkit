"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class OrgsOrgTeamsPostBody(GitHubModel):
    """OrgsOrgTeamsPostBody"""

    name: str = Field(description="The name of the team.")
    description: Missing[str] = Field(
        default=UNSET, description="The description of the team."
    )
    maintainers: Missing[list[str]] = Field(
        default=UNSET,
        description="List GitHub IDs for organization members who will become team maintainers.",
    )
    repo_names: Missing[list[str]] = Field(
        default=UNSET,
        description='The full name (e.g., "organization-name/repository-name") of repositories to add the team to.',
    )
    privacy: Missing[Literal["secret", "closed"]] = Field(
        default=UNSET,
        description="The level of privacy this team should have. The options are:  \n**For a non-nested team:**  \n * `secret` - only visible to organization owners and members of this team.  \n * `closed` - visible to all members of this organization.  \nDefault: `secret`  \n**For a parent or child team:**  \n * `closed` - visible to all members of this organization.  \nDefault for child team: `closed`",
    )
    notification_setting: Missing[
        Literal["notifications_enabled", "notifications_disabled"]
    ] = Field(
        default=UNSET,
        description="The notification setting the team has chosen. The options are:  \n * `notifications_enabled` - team members receive notifications when the team is @mentioned.  \n * `notifications_disabled` - no one receives notifications.  \nDefault: `notifications_enabled`",
    )
    permission: Missing[Literal["pull", "push"]] = Field(
        default=UNSET,
        description="**Closing down notice**. The permission that new repositories will be added to the team with when none is specified.",
    )
    parent_team_id: Missing[int] = Field(
        default=UNSET, description="The ID of a team to set as the parent team."
    )


model_rebuild(OrgsOrgTeamsPostBody)

__all__ = ("OrgsOrgTeamsPostBody",)
