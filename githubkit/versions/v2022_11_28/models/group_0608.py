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
from .group_0418 import WebhooksMembership


class WebhookOrganizationRenamed(GitHubModel):
    """organization renamed event"""

    action: Literal["renamed"] = Field()
    changes: Missing[WebhookOrganizationRenamedPropChanges] = Field(default=UNSET)
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
    membership: Missing[WebhooksMembership] = Field(
        default=UNSET,
        title="Membership",
        description="The membership between the user and the organization. Not present when the action is `member_invited`.",
    )
    organization: OrganizationSimpleWebhooks = Field(
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookOrganizationRenamedPropChanges(GitHubModel):
    """WebhookOrganizationRenamedPropChanges"""

    login: Missing[WebhookOrganizationRenamedPropChangesPropLogin] = Field(
        default=UNSET
    )


class WebhookOrganizationRenamedPropChangesPropLogin(GitHubModel):
    """WebhookOrganizationRenamedPropChangesPropLogin"""

    from_: Missing[str] = Field(default=UNSET, alias="from")


model_rebuild(WebhookOrganizationRenamed)
model_rebuild(WebhookOrganizationRenamedPropChanges)
model_rebuild(WebhookOrganizationRenamedPropChangesPropLogin)

__all__ = (
    "WebhookOrganizationRenamed",
    "WebhookOrganizationRenamedPropChanges",
    "WebhookOrganizationRenamedPropChangesPropLogin",
)
