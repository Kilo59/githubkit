"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0389 import EnterpriseWebhooksType
from .group_0390 import SimpleInstallationType
from .group_0391 import OrganizationSimpleWebhooksType
from .group_0392 import RepositoryWebhooksType
from .group_0614 import WebhookPackageUpdatedPropPackageType


class WebhookPackageUpdatedType(TypedDict):
    """package updated event"""

    action: Literal["updated"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    package: WebhookPackageUpdatedPropPackageType
    repository: RepositoryWebhooksType
    sender: SimpleUserType


__all__ = ("WebhookPackageUpdatedType",)
