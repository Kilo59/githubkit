"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0430 import EnterpriseWebhooks
from .group_0431 import SimpleInstallation
from .group_0432 import OrganizationSimpleWebhooks
from .group_0433 import RepositoryWebhooks


class WebhookMetaDeleted(GitHubModel):
    """meta deleted event"""

    action: Literal["deleted"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/enterprise-cloud@latest//admin/overview/about-enterprise-accounts)."',
    )
    hook: WebhookMetaDeletedPropHook = Field(
        description="The modified webhook. This will contain different keys based on the type of webhook it is: repository, organization, business, app, or GitHub Marketplace."
    )
    hook_id: int = Field(description="The id of the modified webhook.")
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
    repository: Missing[Union[None, RepositoryWebhooks]] = Field(default=UNSET)
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


class WebhookMetaDeletedPropHook(GitHubModel):
    """WebhookMetaDeletedPropHook

    The modified webhook. This will contain different keys based on the type of
    webhook it is: repository, organization, business, app, or GitHub Marketplace.
    """

    active: bool = Field()
    config: WebhookMetaDeletedPropHookPropConfig = Field()
    created_at: str = Field()
    events: list[str] = Field()
    id: int = Field()
    name: str = Field()
    type: str = Field()
    updated_at: str = Field()


class WebhookMetaDeletedPropHookPropConfig(GitHubModel):
    """WebhookMetaDeletedPropHookPropConfig"""

    content_type: Literal["json", "form"] = Field()
    insecure_ssl: str = Field()
    secret: Missing[str] = Field(default=UNSET)
    url: str = Field()


model_rebuild(WebhookMetaDeleted)
model_rebuild(WebhookMetaDeletedPropHook)
model_rebuild(WebhookMetaDeletedPropHookPropConfig)

__all__ = (
    "WebhookMetaDeleted",
    "WebhookMetaDeletedPropHook",
    "WebhookMetaDeletedPropHookPropConfig",
)
