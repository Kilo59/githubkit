"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0428 import WebhooksRelease1Type
from .group_0384 import EnterpriseWebhooksType
from .group_0385 import SimpleInstallationType
from .group_0387 import RepositoryWebhooksType
from .group_0386 import OrganizationSimpleWebhooksType


class WebhookReleaseUnpublishedType(TypedDict):
    """release unpublished event"""

    action: Literal["unpublished"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    release: WebhooksRelease1Type
    repository: RepositoryWebhooksType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookReleaseUnpublishedType",)
