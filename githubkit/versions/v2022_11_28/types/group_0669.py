"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0388 import EnterpriseWebhooksType
from .group_0389 import SimpleInstallationType
from .group_0390 import OrganizationSimpleWebhooksType
from .group_0391 import RepositoryWebhooksType
from .group_0426 import PullRequestWebhookType


class WebhookPullRequestReopenedType(TypedDict):
    """pull_request reopened event"""

    action: Literal["reopened"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    number: int
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pull_request: PullRequestWebhookType
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookPullRequestReopenedType",)
