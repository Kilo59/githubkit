"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0413 import EnterpriseWebhooks
from .group_0414 import SimpleInstallation
from .group_0416 import RepositoryWebhooks
from .group_0417 import SimpleUserWebhooks
from .group_0415 import OrganizationSimpleWebhooks


class WebhookProjectCardDeleted(GitHubModel):
    """project_card deleted event"""

    action: Literal["deleted"] = Field()
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
    project_card: WebhookProjectCardDeletedPropProjectCard = Field(title="Project Card")
    repository: Missing[Union[None, RepositoryWebhooks]] = Field(default=UNSET)
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookProjectCardDeletedPropProjectCard(GitHubModel):
    """Project Card"""

    after_id: Missing[Union[int, None]] = Field(default=UNSET)
    archived: bool = Field(description="Whether or not the card is archived")
    column_id: Union[int, None] = Field()
    column_url: str = Field()
    content_url: Missing[str] = Field(default=UNSET)
    created_at: datetime = Field()
    creator: Union[WebhookProjectCardDeletedPropProjectCardPropCreator, None] = Field(
        title="User"
    )
    id: int = Field(description="The project card's ID")
    node_id: str = Field()
    note: Union[str, None] = Field()
    project_url: str = Field()
    updated_at: datetime = Field()
    url: str = Field()


class WebhookProjectCardDeletedPropProjectCardPropCreator(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookProjectCardDeleted)
model_rebuild(WebhookProjectCardDeletedPropProjectCard)
model_rebuild(WebhookProjectCardDeletedPropProjectCardPropCreator)

__all__ = (
    "WebhookProjectCardDeleted",
    "WebhookProjectCardDeletedPropProjectCard",
    "WebhookProjectCardDeletedPropProjectCardPropCreator",
)
