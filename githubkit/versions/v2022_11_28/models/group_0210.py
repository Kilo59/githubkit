"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0058 import MinimalRepository


class CheckSuitePreference(GitHubModel):
    """Check Suite Preference

    Check suite configuration preferences for a repository.
    """

    preferences: CheckSuitePreferencePropPreferences = Field()
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )


class CheckSuitePreferencePropPreferences(GitHubModel):
    """CheckSuitePreferencePropPreferences"""

    auto_trigger_checks: Missing[
        list[CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItems]
    ] = Field(default=UNSET)


class CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItems(GitHubModel):
    """CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItems"""

    app_id: int = Field()
    setting: bool = Field()


model_rebuild(CheckSuitePreference)
model_rebuild(CheckSuitePreferencePropPreferences)
model_rebuild(CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItems)

__all__ = (
    "CheckSuitePreference",
    "CheckSuitePreferencePropPreferences",
    "CheckSuitePreferencePropPreferencesPropAutoTriggerChecksItems",
)
