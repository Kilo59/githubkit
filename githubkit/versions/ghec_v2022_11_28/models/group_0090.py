"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0091 import (
    EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationId,
)


class EnterpriseRulesetConditionsOrganizationIdTarget(GitHubModel):
    """Repository ruleset conditions for organization IDs

    Parameters for an organization ID condition
    """

    organization_id: EnterpriseRulesetConditionsOrganizationIdTargetPropOrganizationId = Field()


model_rebuild(EnterpriseRulesetConditionsOrganizationIdTarget)

__all__ = ("EnterpriseRulesetConditionsOrganizationIdTarget",)
