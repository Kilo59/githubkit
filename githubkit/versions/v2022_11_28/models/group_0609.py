"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class WebhookRubygemsMetadata(GitHubModel):
    """Ruby Gems metadata"""

    name: Missing[str] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    readme: Missing[str] = Field(default=UNSET)
    homepage: Missing[str] = Field(default=UNSET)
    version_info: Missing[WebhookRubygemsMetadataPropVersionInfo] = Field(default=UNSET)
    platform: Missing[str] = Field(default=UNSET)
    metadata: Missing[WebhookRubygemsMetadataPropMetadata] = Field(default=UNSET)
    repo: Missing[str] = Field(default=UNSET)
    dependencies: Missing[list[WebhookRubygemsMetadataPropDependenciesItems]] = Field(
        default=UNSET
    )
    commit_oid: Missing[str] = Field(default=UNSET)


class WebhookRubygemsMetadataPropVersionInfo(GitHubModel):
    """WebhookRubygemsMetadataPropVersionInfo"""

    version: Missing[str] = Field(default=UNSET)


class WebhookRubygemsMetadataPropMetadata(ExtraGitHubModel):
    """WebhookRubygemsMetadataPropMetadata"""


class WebhookRubygemsMetadataPropDependenciesItems(ExtraGitHubModel):
    """WebhookRubygemsMetadataPropDependenciesItems"""


model_rebuild(WebhookRubygemsMetadata)
model_rebuild(WebhookRubygemsMetadataPropVersionInfo)
model_rebuild(WebhookRubygemsMetadataPropMetadata)
model_rebuild(WebhookRubygemsMetadataPropDependenciesItems)

__all__ = (
    "WebhookRubygemsMetadata",
    "WebhookRubygemsMetadataPropDependenciesItems",
    "WebhookRubygemsMetadataPropMetadata",
    "WebhookRubygemsMetadataPropVersionInfo",
)
