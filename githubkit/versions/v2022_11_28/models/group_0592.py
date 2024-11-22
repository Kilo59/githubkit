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
from .group_0405 import WebhooksMilestone
from .group_0384 import EnterpriseWebhooks
from .group_0385 import SimpleInstallation
from .group_0387 import RepositoryWebhooks
from .group_0386 import OrganizationSimpleWebhooks


class WebhookMilestoneEdited(GitHubModel):
    """milestone edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookMilestoneEditedPropChanges = Field(
        description="The changes to the milestone if the action was `edited`."
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
    milestone: WebhooksMilestone = Field(
        title="Milestone",
        description="A collection of related issues and pull requests.",
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookMilestoneEditedPropChanges(GitHubModel):
    """WebhookMilestoneEditedPropChanges

    The changes to the milestone if the action was `edited`.
    """

    description: Missing[WebhookMilestoneEditedPropChangesPropDescription] = Field(
        default=UNSET
    )
    due_on: Missing[WebhookMilestoneEditedPropChangesPropDueOn] = Field(default=UNSET)
    title: Missing[WebhookMilestoneEditedPropChangesPropTitle] = Field(default=UNSET)


class WebhookMilestoneEditedPropChangesPropDescription(GitHubModel):
    """WebhookMilestoneEditedPropChangesPropDescription"""

    from_: str = Field(
        alias="from",
        description="The previous version of the description if the action was `edited`.",
    )


class WebhookMilestoneEditedPropChangesPropDueOn(GitHubModel):
    """WebhookMilestoneEditedPropChangesPropDueOn"""

    from_: str = Field(
        alias="from",
        description="The previous version of the due date if the action was `edited`.",
    )


class WebhookMilestoneEditedPropChangesPropTitle(GitHubModel):
    """WebhookMilestoneEditedPropChangesPropTitle"""

    from_: str = Field(
        alias="from",
        description="The previous version of the title if the action was `edited`.",
    )


model_rebuild(WebhookMilestoneEdited)
model_rebuild(WebhookMilestoneEditedPropChanges)
model_rebuild(WebhookMilestoneEditedPropChangesPropDescription)
model_rebuild(WebhookMilestoneEditedPropChangesPropDueOn)
model_rebuild(WebhookMilestoneEditedPropChangesPropTitle)

__all__ = (
    "WebhookMilestoneEdited",
    "WebhookMilestoneEditedPropChanges",
    "WebhookMilestoneEditedPropChangesPropDescription",
    "WebhookMilestoneEditedPropChangesPropDueOn",
    "WebhookMilestoneEditedPropChangesPropTitle",
)
