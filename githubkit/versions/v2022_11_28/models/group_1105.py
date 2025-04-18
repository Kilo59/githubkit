"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoNotificationsPutBody(GitHubModel):
    """ReposOwnerRepoNotificationsPutBody"""

    last_read_at: Missing[datetime] = Field(
        default=UNSET,
        description="Describes the last point that notifications were checked. Anything updated since this time will not be marked as read. If you omit this parameter, all notifications are marked as read. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. Default: The current timestamp.",
    )


model_rebuild(ReposOwnerRepoNotificationsPutBody)

__all__ = ("ReposOwnerRepoNotificationsPutBody",)
