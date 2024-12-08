"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import ExtraGitHubModel, GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0657 import WebhookRubygemsMetadata


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersion(GitHubModel):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersion"""

    author: WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthor = Field()
    body: str = Field()
    body_html: str = Field()
    created_at: str = Field()
    description: str = Field()
    docker_metadata: Missing[
        list[
            Union[
                WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMetadataItems,
                None,
            ]
        ]
    ] = Field(default=UNSET)
    draft: Missing[bool] = Field(default=UNSET)
    html_url: str = Field()
    id: int = Field()
    installation_command: str = Field()
    manifest: Missing[str] = Field(default=UNSET)
    metadata: list[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataItems
    ] = Field()
    name: str = Field()
    package_files: list[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFilesItems
    ] = Field()
    package_url: str = Field()
    prerelease: Missing[bool] = Field(default=UNSET)
    release: Missing[
        WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropRelease
    ] = Field(default=UNSET)
    rubygems_metadata: Missing[list[WebhookRubygemsMetadata]] = Field(default=UNSET)
    summary: str = Field()
    tag_name: Missing[str] = Field(default=UNSET)
    target_commitish: str = Field()
    target_oid: str = Field()
    updated_at: str = Field()
    version: str = Field()


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthor(
    GitHubModel
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthor"""

    avatar_url: str = Field()
    events_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    gravatar_id: str = Field()
    html_url: str = Field()
    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organizations_url: str = Field()
    received_events_url: str = Field()
    repos_url: str = Field()
    site_admin: bool = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    type: str = Field()
    url: str = Field()
    user_view_type: Missing[str] = Field(default=UNSET)


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMetadataItems(
    GitHubModel
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMeta
    dataItems
    """

    tags: Missing[list[str]] = Field(default=UNSET)


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataItems(
    ExtraGitHubModel
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataIt
    ems
    """


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFilesItems(
    GitHubModel
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFil
    esItems
    """

    content_type: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    download_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    md5: Missing[Union[str, None]] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    sha1: Missing[Union[str, None]] = Field(default=UNSET)
    sha256: Missing[str] = Field(default=UNSET)
    size: Missing[int] = Field(default=UNSET)
    state: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropRelease(
    GitHubModel
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropRelease"""

    author: WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePropAuthor = Field()
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


class WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePropAuthor(
    GitHubModel
):
    """WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePro
    pAuthor
    """

    avatar_url: str = Field()
    events_url: str = Field()
    followers_url: str = Field()
    following_url: str = Field()
    gists_url: str = Field()
    gravatar_id: str = Field()
    html_url: str = Field()
    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organizations_url: str = Field()
    received_events_url: str = Field()
    repos_url: str = Field()
    site_admin: bool = Field()
    starred_url: str = Field()
    subscriptions_url: str = Field()
    type: str = Field()
    url: str = Field()
    user_view_type: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersion)
model_rebuild(
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthor
)
model_rebuild(
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMetadataItems
)
model_rebuild(
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataItems
)
model_rebuild(
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFilesItems
)
model_rebuild(
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropRelease
)
model_rebuild(
    WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePropAuthor
)

__all__ = (
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersion",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropAuthor",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropDockerMetadataItems",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropMetadataItems",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropPackageFilesItems",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropRelease",
    "WebhookRegistryPackageUpdatedPropRegistryPackagePropPackageVersionPropReleasePropAuthor",
)
