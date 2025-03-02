"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0018 import InstallationType
from .group_0458 import EnterpriseWebhooksType
from .group_0460 import OrganizationSimpleWebhooksType
from .group_0461 import RepositoryWebhooksType
from .group_0471 import WebhooksUserType
from .group_0476 import WebhooksRepositoriesItemsType


class WebhookInstallationCreatedType(TypedDict):
    """installation created event"""

    action: Literal["created"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[list[WebhooksRepositoriesItemsType]]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[Union[WebhooksUserType, None]]
    sender: SimpleUserType


__all__ = ("WebhookInstallationCreatedType",)
