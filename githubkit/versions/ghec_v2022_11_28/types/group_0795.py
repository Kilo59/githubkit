"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0191 import FullRepositoryType
from .group_0439 import EnterpriseWebhooksType
from .group_0440 import SimpleInstallationType
from .group_0441 import OrganizationSimpleWebhooksType
from .group_0796 import WebhookSecurityAndAnalysisPropChangesType


class WebhookSecurityAndAnalysisType(TypedDict):
    """security_and_analysis event"""

    changes: WebhookSecurityAndAnalysisPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: FullRepositoryType
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookSecurityAndAnalysisType",)
