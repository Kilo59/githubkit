"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0029 import CodeScanningDefaultSetupOptionsType


class OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyType(TypedDict):
    """OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBody"""

    name: NotRequired[str]
    description: NotRequired[str]
    advanced_security: NotRequired[Literal["enabled", "disabled"]]
    dependency_graph: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependency_graph_autosubmit_action: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    dependency_graph_autosubmit_action_options: NotRequired[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType
    ]
    dependabot_alerts: NotRequired[Literal["enabled", "disabled", "not_set"]]
    dependabot_security_updates: NotRequired[Literal["enabled", "disabled", "not_set"]]
    code_scanning_default_setup: NotRequired[Literal["enabled", "disabled", "not_set"]]
    code_scanning_default_setup_options: NotRequired[
        Union[CodeScanningDefaultSetupOptionsType, None]
    ]
    secret_scanning: NotRequired[Literal["enabled", "disabled", "not_set"]]
    secret_scanning_push_protection: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_delegated_bypass: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_delegated_bypass_options: NotRequired[
        OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDelegatedBypassOptionsType
    ]
    secret_scanning_validity_checks: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_non_provider_patterns: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    secret_scanning_delegated_alert_dismissal: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    private_vulnerability_reporting: NotRequired[
        Literal["enabled", "disabled", "not_set"]
    ]
    enforcement: NotRequired[Literal["enforced", "unenforced"]]


class OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType(
    TypedDict
):
    """OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAuto
    submitActionOptions

    Feature options for Automatic dependency submission
    """

    labeled_runners: NotRequired[bool]


class OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDelegatedBypassOptionsType(
    TypedDict
):
    """OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDeleg
    atedBypassOptions

    Feature options for secret scanning delegated bypass
    """

    reviewers: NotRequired[
        list[
            OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItemsType
        ]
    ]


class OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItemsType(
    TypedDict
):
    """OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDeleg
    atedBypassOptionsPropReviewersItems
    """

    reviewer_id: int
    reviewer_type: Literal["TEAM", "ROLE"]


__all__ = (
    "OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropDependencyGraphAutosubmitActionOptionsType",
    "OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDelegatedBypassOptionsPropReviewersItemsType",
    "OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyPropSecretScanningDelegatedBypassOptionsType",
    "OrgsOrgCodeSecurityConfigurationsConfigurationIdPatchBodyType",
)
