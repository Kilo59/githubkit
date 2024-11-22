"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0073 import MilestoneType
from .group_0002 import SimpleUserType
from .group_0427 import EnterpriseWebhooksType
from .group_0430 import RepositoryWebhooksType
from .group_0469 import WebhooksPullRequest5Type
from .group_0429 import OrganizationSimpleWebhooksType


class WebhookPullRequestDemilestonedType(TypedDict):
    """pull_request demilestoned event"""

    action: Literal["demilestoned"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    milestone: NotRequired[MilestoneType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: WebhooksPullRequest5Type
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookPullRequestDemilestonedType",)
