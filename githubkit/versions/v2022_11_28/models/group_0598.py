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

from .group_0002 import SimpleUser
from .group_0395 import WebhooksUser
from .group_0384 import EnterpriseWebhooks
from .group_0385 import SimpleInstallation
from .group_0387 import RepositoryWebhooks
from .group_0386 import OrganizationSimpleWebhooks


class WebhookOrganizationMemberInvited(GitHubModel):
    """organization member_invited event"""

    action: Literal["member_invited"] = Field()
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
    invitation: WebhookOrganizationMemberInvitedPropInvitation = Field(
        description="The invitation for the user or email if the action is `member_invited`."
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
    user: Missing[Union[WebhooksUser, None]] = Field(default=UNSET, title="User")


class WebhookOrganizationMemberInvitedPropInvitation(GitHubModel):
    """WebhookOrganizationMemberInvitedPropInvitation

    The invitation for the user or email if the action is `member_invited`.
    """

    created_at: datetime = Field()
    email: Union[str, None] = Field()
    failed_at: Union[datetime, None] = Field()
    failed_reason: Union[str, None] = Field()
    id: float = Field()
    invitation_teams_url: str = Field()
    inviter: Union[WebhookOrganizationMemberInvitedPropInvitationPropInviter, None] = (
        Field(title="User")
    )
    login: Union[str, None] = Field()
    node_id: str = Field()
    role: str = Field()
    team_count: float = Field()
    invitation_source: Missing[str] = Field(default=UNSET)


class WebhookOrganizationMemberInvitedPropInvitationPropInviter(GitHubModel):
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
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookOrganizationMemberInvited)
model_rebuild(WebhookOrganizationMemberInvitedPropInvitation)
model_rebuild(WebhookOrganizationMemberInvitedPropInvitationPropInviter)

__all__ = (
    "WebhookOrganizationMemberInvited",
    "WebhookOrganizationMemberInvitedPropInvitation",
    "WebhookOrganizationMemberInvitedPropInvitationPropInviter",
)
