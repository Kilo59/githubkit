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
from .group_0389 import EnterpriseWebhooks
from .group_0390 import SimpleInstallation
from .group_0391 import OrganizationSimpleWebhooks
from .group_0392 import RepositoryWebhooks
from .group_0421 import WebhooksProject


class WebhookProjectEdited(GitHubModel):
    """project edited event"""

    action: Literal["edited"] = Field()
    changes: Missing[WebhookProjectEditedPropChanges] = Field(
        default=UNSET,
        description="The changes to the project if the action was `edited`.",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    project: WebhooksProject = Field(title="Project")
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


class WebhookProjectEditedPropChanges(GitHubModel):
    """WebhookProjectEditedPropChanges

    The changes to the project if the action was `edited`.
    """

    body: Missing[WebhookProjectEditedPropChangesPropBody] = Field(default=UNSET)
    name: Missing[WebhookProjectEditedPropChangesPropName] = Field(default=UNSET)


class WebhookProjectEditedPropChangesPropBody(GitHubModel):
    """WebhookProjectEditedPropChangesPropBody"""

    from_: str = Field(
        alias="from",
        description="The previous version of the body if the action was `edited`.",
    )


class WebhookProjectEditedPropChangesPropName(GitHubModel):
    """WebhookProjectEditedPropChangesPropName"""

    from_: str = Field(
        alias="from",
        description="The changes to the project if the action was `edited`.",
    )


model_rebuild(WebhookProjectEdited)
model_rebuild(WebhookProjectEditedPropChanges)
model_rebuild(WebhookProjectEditedPropChangesPropBody)
model_rebuild(WebhookProjectEditedPropChangesPropName)

__all__ = (
    "WebhookProjectEdited",
    "WebhookProjectEditedPropChanges",
    "WebhookProjectEditedPropChangesPropBody",
    "WebhookProjectEditedPropChangesPropName",
)
