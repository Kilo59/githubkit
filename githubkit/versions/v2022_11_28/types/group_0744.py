"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0388 import EnterpriseWebhooksType
from .group_0389 import SimpleInstallationType
from .group_0390 import OrganizationSimpleWebhooksType
from .group_0391 import RepositoryWebhooksType
from .group_0436 import WebhooksSponsorshipType
from .group_0437 import WebhooksChanges8Type


class WebhookSponsorshipTierChangedType(TypedDict):
    """sponsorship tier_changed event"""

    action: Literal["tier_changed"]
    changes: WebhooksChanges8Type
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType
    sponsorship: WebhooksSponsorshipType


__all__ = ("WebhookSponsorshipTierChangedType",)
