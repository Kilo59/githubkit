"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0016 import AppPermissionsType


class AppInstallationsInstallationIdAccessTokensPostBodyType(TypedDict):
    """AppInstallationsInstallationIdAccessTokensPostBody"""

    repositories: NotRequired[list[str]]
    repository_ids: NotRequired[list[int]]
    permissions: NotRequired[AppPermissionsType]


__all__ = ("AppInstallationsInstallationIdAccessTokensPostBodyType",)
