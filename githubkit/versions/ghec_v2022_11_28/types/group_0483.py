"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0414 import SimpleInstallationType
from .group_0416 import RepositoryWebhooksType
from .group_0417 import SimpleUserWebhooksType
from .group_0415 import OrganizationSimpleWebhooksType
from .group_0422 import CheckRunWithSimpleCheckSuiteType


class WebhookCheckRunRerequestedType(TypedDict):
    """Check Run Re-Requested Event"""

    action: Literal["rerequested"]
    check_run: CheckRunWithSimpleCheckSuiteType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookCheckRunRerequestedType",)
