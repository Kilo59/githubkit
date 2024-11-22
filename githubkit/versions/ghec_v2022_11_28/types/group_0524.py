"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0215 import DeploymentType
from .group_0343 import PullRequestType
from .group_0428 import SimpleInstallationType
from .group_0430 import RepositoryWebhooksType
from .group_0429 import OrganizationSimpleWebhooksType


class WebhookDeploymentProtectionRuleRequestedType(TypedDict):
    """deployment protection rule requested event"""

    action: Literal["requested"]
    environment: NotRequired[str]
    event: NotRequired[str]
    deployment_callback_url: NotRequired[str]
    deployment: NotRequired[DeploymentType]
    pull_requests: NotRequired[list[PullRequestType]]
    repository: NotRequired[RepositoryWebhooksType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    sender: NotRequired[SimpleUserType]


__all__ = ("WebhookDeploymentProtectionRuleRequestedType",)
