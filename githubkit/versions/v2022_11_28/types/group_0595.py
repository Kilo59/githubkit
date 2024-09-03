"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0376 import EnterpriseWebhooksType
from .group_0377 import SimpleInstallationType
from .group_0379 import RepositoryWebhooksType
from .group_0380 import SimpleUserWebhooksType
from .group_0378 import OrganizationSimpleWebhooksType
from .group_0596 import WebhookPackagePublishedPropPackageType


class WebhookPackagePublishedType(TypedDict):
    """package published event"""

    action: Literal["published"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    package: WebhookPackagePublishedPropPackageType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserWebhooksType


__all__ = ("WebhookPackagePublishedType",)
