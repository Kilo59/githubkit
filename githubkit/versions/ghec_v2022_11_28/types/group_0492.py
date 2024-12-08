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
from .group_0433 import RepositoryWebhooksType
from .group_0435 import ExemptionResponseType
from .group_0436 import ExemptionRequestType


class WebhookExemptionRequestResponseSubmittedType(TypedDict):
    """Exemption response submitted event"""

    action: Literal["response_submitted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    exemption_request: ExemptionRequestType
    exemption_response: ExemptionResponseType
    sender: SimpleUserType


__all__ = ("WebhookExemptionRequestResponseSubmittedType",)
