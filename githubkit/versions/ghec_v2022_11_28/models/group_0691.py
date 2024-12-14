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

from .group_0002 import SimpleUser
from .group_0439 import EnterpriseWebhooks
from .group_0440 import SimpleInstallation
from .group_0441 import OrganizationSimpleWebhooks
from .group_0442 import RepositoryWebhooks
from .group_0474 import WebhooksProjectColumn


class WebhookProjectColumnEdited(GitHubModel):
    """project_column edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookProjectColumnEditedPropChanges = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/enterprise-cloud@latest//apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    project_column: WebhooksProjectColumn = Field(title="Project Column")
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


class WebhookProjectColumnEditedPropChanges(GitHubModel):
    """WebhookProjectColumnEditedPropChanges"""

    name: Missing[WebhookProjectColumnEditedPropChangesPropName] = Field(default=UNSET)


class WebhookProjectColumnEditedPropChangesPropName(GitHubModel):
    """WebhookProjectColumnEditedPropChangesPropName"""

    from_: str = Field(alias="from")


model_rebuild(WebhookProjectColumnEdited)
model_rebuild(WebhookProjectColumnEditedPropChanges)
model_rebuild(WebhookProjectColumnEditedPropChangesPropName)

__all__ = (
    "WebhookProjectColumnEdited",
    "WebhookProjectColumnEditedPropChanges",
    "WebhookProjectColumnEditedPropChangesPropName",
)
