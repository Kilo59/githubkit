"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0439 import EnterpriseWebhooksType
from .group_0440 import SimpleInstallationType
from .group_0441 import OrganizationSimpleWebhooksType
from .group_0442 import RepositoryWebhooksType
from .group_0746 import WebhookRegistryPackagePublishedPropRegistryPackageType


class WebhookRegistryPackagePublishedType(TypedDict):
    """WebhookRegistryPackagePublished"""

    action: Literal["published"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    registry_package: WebhookRegistryPackagePublishedPropRegistryPackageType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


__all__ = ("WebhookRegistryPackagePublishedType",)
