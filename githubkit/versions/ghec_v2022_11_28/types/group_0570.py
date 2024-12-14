"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0017 import InstallationType
from .group_0439 import EnterpriseWebhooksType
from .group_0441 import OrganizationSimpleWebhooksType
from .group_0442 import RepositoryWebhooksType
from .group_0452 import WebhooksUserType
from .group_0458 import WebhooksRepositoriesAddedItemsType


class WebhookInstallationRepositoriesAddedType(TypedDict):
    """installation_repositories added event"""

    action: Literal["added"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: InstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repositories_added: list[WebhooksRepositoriesAddedItemsType]
    repositories_removed: list[
        WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType
    ]
    repository: NotRequired[RepositoryWebhooksType]
    repository_selection: Literal["all", "selected"]
    requester: Union[WebhooksUserType, None]
    sender: SimpleUserType


class WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType(TypedDict):
    """WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItems"""

    full_name: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[str]
    node_id: NotRequired[str]
    private: NotRequired[bool]


__all__ = (
    "WebhookInstallationRepositoriesAddedPropRepositoriesRemovedItemsType",
    "WebhookInstallationRepositoriesAddedType",
)
