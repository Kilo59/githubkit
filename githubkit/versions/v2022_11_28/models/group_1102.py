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


class UserCodespacesPostBodyOneof0(GitHubModel):
    """UserCodespacesPostBodyOneof0"""

    repository_id: int = Field(description="Repository id for this codespace")
    ref: Missing[str] = Field(
        default=UNSET,
        description="Git ref (typically a branch name) for this codespace",
    )
    location: Missing[str] = Field(
        default=UNSET,
        description="The requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.",
    )
    geo: Missing[Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"]] = Field(
        default=UNSET,
        description="The geographic area for this codespace. If not specified, the value is assigned by IP. This property replaces `location`, which is closing down.",
    )
    client_ip: Missing[str] = Field(
        default=UNSET,
        description="IP for location auto-detection when proxying a request",
    )
    machine: Missing[str] = Field(
        default=UNSET, description="Machine type to use for this codespace"
    )
    devcontainer_path: Missing[str] = Field(
        default=UNSET,
        description="Path to devcontainer.json config to use for this codespace",
    )
    multi_repo_permissions_opt_out: Missing[bool] = Field(
        default=UNSET,
        description="Whether to authorize requested permissions from devcontainer.json",
    )
    working_directory: Missing[str] = Field(
        default=UNSET, description="Working directory for this codespace"
    )
    idle_timeout_minutes: Missing[int] = Field(
        default=UNSET,
        description="Time in minutes before codespace stops from inactivity",
    )
    display_name: Missing[str] = Field(
        default=UNSET, description="Display name for this codespace"
    )
    retention_period_minutes: Missing[int] = Field(
        default=UNSET,
        description="Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).",
    )


model_rebuild(UserCodespacesPostBodyOneof0)

__all__ = ("UserCodespacesPostBodyOneof0",)
