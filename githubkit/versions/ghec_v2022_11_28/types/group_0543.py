"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0015 import InstallationType
from .group_0413 import EnterpriseWebhooksType
from .group_0416 import RepositoryWebhooksType
from .group_0417 import SimpleUserWebhooksType
from .group_0432 import WebhooksRepositoriesItemsType
from .group_0415 import OrganizationSimpleWebhooksType


class WebhookInstallationDeletedType(TypedDict):
    """installation deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories: NotRequired[List[WebhooksRepositoriesItemsType]]
    repository: NotRequired[RepositoryWebhooksType]
    requester: NotRequired[None]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookInstallationDeletedType",)
