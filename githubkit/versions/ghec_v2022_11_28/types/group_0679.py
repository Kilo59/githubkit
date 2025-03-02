"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0458 import EnterpriseWebhooksType
from .group_0459 import SimpleInstallationType
from .group_0460 import OrganizationSimpleWebhooksType
from .group_0461 import RepositoryWebhooksType
from .group_0471 import WebhooksUserType


class WebhookOrgBlockUnblockedType(TypedDict):
    """org_block unblocked event"""

    action: Literal["unblocked"]
    blocked_user: Union[WebhooksUserType, None]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


__all__ = ("WebhookOrgBlockUnblockedType",)
