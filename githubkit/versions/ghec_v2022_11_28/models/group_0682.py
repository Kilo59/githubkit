"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0463 import ProjectsV2
from .group_0428 import SimpleInstallation
from .group_0429 import OrganizationSimpleWebhooks


class WebhookProjectsV2ProjectClosed(GitHubModel):
    """Projects v2 Project Closed Event"""

    action: Literal["closed"] = Field()
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    projects_v2: ProjectsV2 = Field(
        title="Projects v2 Project", description="A projects v2 project"
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


model_rebuild(WebhookProjectsV2ProjectClosed)

__all__ = ("WebhookProjectsV2ProjectClosed",)
