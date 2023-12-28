"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import WebhookDeploymentProtectionRuleRequested

Event: TypeAlias = WebhookDeploymentProtectionRuleRequested

DeploymentProtectionRuleEvent: TypeAlias = Event

action_types = WebhookDeploymentProtectionRuleRequested

deployment_protection_rule_action_types = action_types

__all__ = (
    "Event",
    "DeploymentProtectionRuleEvent",
    "action_types",
    "deployment_protection_rule_action_types",
)
