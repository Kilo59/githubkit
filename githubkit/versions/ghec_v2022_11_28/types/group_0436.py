"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0435 import ExemptionResponseType


class ExemptionRequestType(TypedDict):
    """Exemption Request

    A request from a user to be exempted from a set of rules.
    """

    id: NotRequired[int]
    number: NotRequired[int]
    repository_id: NotRequired[int]
    requester_id: NotRequired[int]
    requester_login: NotRequired[str]
    request_type: NotRequired[Literal["push_ruleset_bypass", "secret_scanning"]]
    exemption_request_data: NotRequired[
        Union[ExemptionRequestPushRulesetBypassType, ExemptionRequestSecretScanningType]
    ]
    resource_identifier: NotRequired[str]
    status: NotRequired[Literal["pending", "rejected", "cancelled", "completed"]]
    requester_comment: NotRequired[Union[str, None]]
    metadata: NotRequired[Union[ExemptionRequestSecretScanningMetadataType, None]]
    expires_at: NotRequired[datetime]
    created_at: NotRequired[datetime]
    responses: NotRequired[Union[list[ExemptionResponseType], None]]
    html_url: NotRequired[str]


class ExemptionRequestSecretScanningMetadataType(TypedDict):
    """Secret Scanning Push Protection Exemption Request Metadata

    Metadata for a secret scanning push protection exemption request.
    """

    label: NotRequired[str]
    reason: NotRequired[Literal["fixed_later", "false_positive", "tests"]]


class ExemptionRequestPushRulesetBypassType(TypedDict):
    """Push ruleset bypass exemption request data

    Push rules that are being requested to be bypassed.
    """

    type: NotRequired[Literal["push_ruleset_bypass"]]
    data: NotRequired[list[ExemptionRequestPushRulesetBypassPropDataItemsType]]


class ExemptionRequestPushRulesetBypassPropDataItemsType(TypedDict):
    """ExemptionRequestPushRulesetBypassPropDataItems"""

    ruleset_id: NotRequired[int]
    ruleset_name: NotRequired[str]
    total_violations: NotRequired[int]
    rule_type: NotRequired[str]


class ExemptionRequestSecretScanningType(TypedDict):
    """Secret scanning push protection exemption request data

    Secret scanning push protections that are being requested to be bypassed.
    """

    type: NotRequired[Literal["secret_scanning"]]
    data: NotRequired[list[ExemptionRequestSecretScanningPropDataItemsType]]


class ExemptionRequestSecretScanningPropDataItemsType(TypedDict):
    """ExemptionRequestSecretScanningPropDataItems"""

    secret_type: NotRequired[str]
    locations: NotRequired[
        list[ExemptionRequestSecretScanningPropDataItemsPropLocationsItemsType]
    ]


class ExemptionRequestSecretScanningPropDataItemsPropLocationsItemsType(TypedDict):
    """ExemptionRequestSecretScanningPropDataItemsPropLocationsItems"""

    commit: NotRequired[str]
    branch: NotRequired[str]
    path: NotRequired[str]


__all__ = (
    "ExemptionRequestPushRulesetBypassPropDataItemsType",
    "ExemptionRequestPushRulesetBypassType",
    "ExemptionRequestSecretScanningMetadataType",
    "ExemptionRequestSecretScanningPropDataItemsPropLocationsItemsType",
    "ExemptionRequestSecretScanningPropDataItemsType",
    "ExemptionRequestSecretScanningType",
    "ExemptionRequestType",
)
