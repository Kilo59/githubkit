"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0430 import EnterpriseWebhooksType
from .group_0431 import SimpleInstallationType
from .group_0432 import OrganizationSimpleWebhooksType
from .group_0433 import RepositoryWebhooksType


class WebhookRepositoryRenamedType(TypedDict):
    """repository renamed event"""

    action: Literal["renamed"]
    changes: WebhookRepositoryRenamedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookRepositoryRenamedPropChangesType(TypedDict):
    """WebhookRepositoryRenamedPropChanges"""

    repository: WebhookRepositoryRenamedPropChangesPropRepositoryType


class WebhookRepositoryRenamedPropChangesPropRepositoryType(TypedDict):
    """WebhookRepositoryRenamedPropChangesPropRepository"""

    name: WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType


class WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType(TypedDict):
    """WebhookRepositoryRenamedPropChangesPropRepositoryPropName"""

    from_: str


__all__ = (
    "WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType",
    "WebhookRepositoryRenamedPropChangesPropRepositoryType",
    "WebhookRepositoryRenamedPropChangesType",
    "WebhookRepositoryRenamedType",
)
