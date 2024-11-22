"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0461 import WebhooksProjectType
from .group_0427 import EnterpriseWebhooksType
from .group_0428 import SimpleInstallationType
from .group_0430 import RepositoryWebhooksType
from .group_0429 import OrganizationSimpleWebhooksType


class WebhookProjectReopenedType(TypedDict):
    """project reopened event"""

    action: Literal["reopened"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhooksProjectType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


__all__ = ("WebhookProjectReopenedType",)
