"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0546 import (
    WebhookIssuesClosedPropIssueAllof0PropPerformedViaGithubAppPropOwner,
    WebhookIssuesClosedPropIssueAllof0PropPerformedViaGithubAppPropPermissions,
)


class WebhookIssuesClosedPropIssueAllof0PropPerformedViaGithubApp(GitHubModel):
    """App

    GitHub apps are a new way to extend GitHub. They can be installed directly on
    organizations and user accounts and granted access to specific repositories.
    They come with granular permissions and built-in webhooks. GitHub apps are first
    class actors within GitHub.
    """

    created_at: Union[datetime, None] = Field()
    description: Union[str, None] = Field()
    events: Missing[List[str]] = Field(
        default=UNSET, description="The list of events for the GitHub app"
    )
    external_url: Union[str, None] = Field()
    html_url: str = Field()
    id: Union[int, None] = Field(description="Unique identifier of the GitHub app")
    name: str = Field(description="The name of the GitHub app")
    node_id: str = Field()
    owner: Union[
        WebhookIssuesClosedPropIssueAllof0PropPerformedViaGithubAppPropOwner, None
    ] = Field(title="User")
    permissions: Missing[
        WebhookIssuesClosedPropIssueAllof0PropPerformedViaGithubAppPropPermissions
    ] = Field(default=UNSET, description="The set of permissions for the GitHub app")
    slug: Missing[str] = Field(
        default=UNSET, description="The slug name of the GitHub app"
    )
    updated_at: Union[datetime, None] = Field()


model_rebuild(WebhookIssuesClosedPropIssueAllof0PropPerformedViaGithubApp)

__all__ = ("WebhookIssuesClosedPropIssueAllof0PropPerformedViaGithubApp",)
