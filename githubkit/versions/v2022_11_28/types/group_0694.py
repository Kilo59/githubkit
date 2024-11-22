"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0154 import RepositoryAdvisoryType
from .group_0384 import EnterpriseWebhooksType
from .group_0385 import SimpleInstallationType
from .group_0387 import RepositoryWebhooksType
from .group_0386 import OrganizationSimpleWebhooksType


class WebhookRepositoryAdvisoryReportedType(TypedDict):
    """Repository advisory reported event"""

    action: Literal["reported"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    repository_advisory: RepositoryAdvisoryType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookRepositoryAdvisoryReportedType",)
