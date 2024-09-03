"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0675 import (
    WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersion,
)


class WebhookRegistryPackagePublishedPropRegistryPackage(GitHubModel):
    """WebhookRegistryPackagePublishedPropRegistryPackage"""

    created_at: Union[str, None] = Field()
    description: Union[str, None] = Field()
    ecosystem: str = Field()
    html_url: str = Field()
    id: int = Field()
    name: str = Field()
    namespace: str = Field()
    owner: WebhookRegistryPackagePublishedPropRegistryPackagePropOwner = Field()
    package_type: str = Field()
    package_version: Union[
        WebhookRegistryPackagePublishedPropRegistryPackagePropPackageVersion, None
    ] = Field()
    registry: Union[
        WebhookRegistryPackagePublishedPropRegistryPackagePropRegistry, None
    ] = Field()
    updated_at: Union[str, None] = Field()


class WebhookRegistryPackagePublishedPropRegistryPackagePropOwner(GitHubModel):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropOwner"""

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


class WebhookRegistryPackagePublishedPropRegistryPackagePropRegistry(GitHubModel):
    """WebhookRegistryPackagePublishedPropRegistryPackagePropRegistry"""

    about_url: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    vendor: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookRegistryPackagePublishedPropRegistryPackage)
model_rebuild(WebhookRegistryPackagePublishedPropRegistryPackagePropOwner)
model_rebuild(WebhookRegistryPackagePublishedPropRegistryPackagePropRegistry)

__all__ = (
    "WebhookRegistryPackagePublishedPropRegistryPackage",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropOwner",
    "WebhookRegistryPackagePublishedPropRegistryPackagePropRegistry",
)
