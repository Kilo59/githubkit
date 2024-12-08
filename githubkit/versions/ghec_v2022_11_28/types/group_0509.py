"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0430 import EnterpriseWebhooksType
from .group_0431 import SimpleInstallationType
from .group_0432 import OrganizationSimpleWebhooksType
from .group_0433 import RepositoryWebhooksType


class WebhookCodeScanningAlertReopenedByUserType(TypedDict):
    """code_scanning_alert reopened_by_user event"""

    action: Literal["reopened_by_user"]
    alert: WebhookCodeScanningAlertReopenedByUserPropAlertType
    commit_oid: str
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    ref: str
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookCodeScanningAlertReopenedByUserPropAlertType(TypedDict):
    """WebhookCodeScanningAlertReopenedByUserPropAlert

    The code scanning alert involved in the event.
    """

    created_at: datetime
    dismissed_at: None
    dismissed_by: None
    dismissed_reason: None
    html_url: str
    most_recent_instance: NotRequired[
        Union[
            WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstanceType,
            None,
        ]
    ]
    number: int
    rule: WebhookCodeScanningAlertReopenedByUserPropAlertPropRuleType
    state: Literal["open", "fixed"]
    tool: WebhookCodeScanningAlertReopenedByUserPropAlertPropToolType
    url: str


class WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstanceType(
    TypedDict
):
    """Alert Instance"""

    analysis_key: str
    category: NotRequired[str]
    classifications: NotRequired[list[str]]
    commit_sha: NotRequired[str]
    environment: str
    location: NotRequired[
        WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocationType
    ]
    message: NotRequired[
        WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessageType
    ]
    ref: str
    state: Literal["open", "dismissed", "fixed"]


class WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocationType(
    TypedDict
):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocatio
    n
    """

    end_column: NotRequired[int]
    end_line: NotRequired[int]
    path: NotRequired[str]
    start_column: NotRequired[int]
    start_line: NotRequired[int]


class WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessageType(
    TypedDict
):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessage"""

    text: NotRequired[str]


class WebhookCodeScanningAlertReopenedByUserPropAlertPropRuleType(TypedDict):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropRule"""

    description: str
    id: str
    severity: Union[None, Literal["none", "note", "warning", "error"]]


class WebhookCodeScanningAlertReopenedByUserPropAlertPropToolType(TypedDict):
    """WebhookCodeScanningAlertReopenedByUserPropAlertPropTool"""

    name: str
    version: Union[str, None]


__all__ = (
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropLocationType",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstancePropMessageType",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropMostRecentInstanceType",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropRuleType",
    "WebhookCodeScanningAlertReopenedByUserPropAlertPropToolType",
    "WebhookCodeScanningAlertReopenedByUserPropAlertType",
    "WebhookCodeScanningAlertReopenedByUserType",
)
