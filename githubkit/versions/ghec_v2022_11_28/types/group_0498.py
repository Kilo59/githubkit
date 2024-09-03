"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0121 import CustomPropertyType
from .group_0413 import EnterpriseWebhooksType
from .group_0414 import SimpleInstallationType
from .group_0417 import SimpleUserWebhooksType
from .group_0415 import OrganizationSimpleWebhooksType


class WebhookCustomPropertyUpdatedType(TypedDict):
    """custom property updated event"""

    action: Literal["updated"]
    definition: CustomPropertyType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookCustomPropertyUpdatedType",)
