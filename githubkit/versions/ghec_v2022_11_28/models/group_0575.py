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

from .group_0003 import SimpleUser
from .group_0460 import OrganizationSimpleWebhooks
from .group_0461 import RepositoryWebhooks
from .group_0472 import WebhooksAnswer
from .group_0473 import Discussion


class WebhookDiscussionUnanswered(GitHubModel):
    """discussion unanswered event"""

    action: Literal["unanswered"] = Field()
    discussion: Discussion = Field(
        title="Discussion", description="A Discussion in a repository."
    )
    old_answer: WebhooksAnswer = Field()
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUser] = Field(
        default=UNSET, title="Simple User", description="A GitHub user."
    )


model_rebuild(WebhookDiscussionUnanswered)

__all__ = ("WebhookDiscussionUnanswered",)
