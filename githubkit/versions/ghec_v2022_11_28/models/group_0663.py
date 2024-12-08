"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0657 import WebhookRubygemsMetadata


class WebhookPackageUpdatedPropPackagePropPackageVersion(GitHubModel):
    """WebhookPackageUpdatedPropPackagePropPackageVersion"""

    author: Union[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropAuthor, None
    ] = Field(title="User")
    body: str = Field()
    body_html: str = Field()
    created_at: str = Field()
    description: str = Field()
    docker_metadata: Missing[
        list[WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItems]
    ] = Field(default=UNSET)
    draft: Missing[bool] = Field(default=UNSET)
    html_url: str = Field()
    id: int = Field()
    installation_command: str = Field()
    manifest: Missing[str] = Field(default=UNSET)
    metadata: list[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItems
    ] = Field()
    name: str = Field()
    package_files: list[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItems
    ] = Field()
    package_url: Missing[str] = Field(default=UNSET)
    prerelease: Missing[bool] = Field(default=UNSET)
    release: Missing[WebhookPackageUpdatedPropPackagePropPackageVersionPropRelease] = (
        Field(default=UNSET)
    )
    rubygems_metadata: Missing[list[WebhookRubygemsMetadata]] = Field(default=UNSET)
    source_url: Missing[str] = Field(default=UNSET)
    summary: str = Field()
    tag_name: Missing[str] = Field(default=UNSET)
    target_commitish: str = Field()
    target_oid: str = Field()
    updated_at: str = Field()
    version: str = Field()


class WebhookPackageUpdatedPropPackagePropPackageVersionPropAuthor(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItems(
    GitHubModel
):
    """WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItems"""

    tags: Missing[list[str]] = Field(default=UNSET)


class WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItems(
    ExtraGitHubModel
):
    """WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItems"""


class WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItems(
    GitHubModel
):
    """WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItems"""

    content_type: str = Field()
    created_at: str = Field()
    download_url: str = Field()
    id: int = Field()
    md5: Union[str, None] = Field()
    name: str = Field()
    sha1: Union[str, None] = Field()
    sha256: str = Field()
    size: int = Field()
    state: str = Field()
    updated_at: str = Field()


class WebhookPackageUpdatedPropPackagePropPackageVersionPropRelease(GitHubModel):
    """WebhookPackageUpdatedPropPackagePropPackageVersionPropRelease"""

    author: Union[
        WebhookPackageUpdatedPropPackagePropPackageVersionPropReleasePropAuthor, None
    ] = Field(title="User")
    created_at: str = Field()
    draft: bool = Field()
    html_url: str = Field()
    id: int = Field()
    name: str = Field()
    prerelease: bool = Field()
    published_at: str = Field()
    tag_name: str = Field()
    target_commitish: str = Field()
    url: str = Field()


class WebhookPackageUpdatedPropPackagePropPackageVersionPropReleasePropAuthor(
    GitHubModel
):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookPackageUpdatedPropPackagePropPackageVersion)
model_rebuild(WebhookPackageUpdatedPropPackagePropPackageVersionPropAuthor)
model_rebuild(WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItems)
model_rebuild(WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItems)
model_rebuild(WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItems)
model_rebuild(WebhookPackageUpdatedPropPackagePropPackageVersionPropRelease)
model_rebuild(WebhookPackageUpdatedPropPackagePropPackageVersionPropReleasePropAuthor)

__all__ = (
    "WebhookPackageUpdatedPropPackagePropPackageVersion",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropAuthor",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropDockerMetadataItems",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropMetadataItems",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropPackageFilesItems",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropRelease",
    "WebhookPackageUpdatedPropPackagePropPackageVersionPropReleasePropAuthor",
)
