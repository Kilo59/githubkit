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
from .group_0462 import PersonalAccessTokenRequestType


class WebhookPersonalAccessTokenRequestDeniedType(TypedDict):
    """personal_access_token_request denied event"""

    action: Literal["denied"]
    personal_access_token_request: PersonalAccessTokenRequestType
    organization: OrganizationSimpleWebhooksType
    enterprise: NotRequired[EnterpriseWebhooksType]
    sender: SimpleUserType
    installation: SimpleInstallationType


__all__ = ("WebhookPersonalAccessTokenRequestDeniedType",)
