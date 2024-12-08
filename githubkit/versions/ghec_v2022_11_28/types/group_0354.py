"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0075 import ReactionRollupType
from .group_0353 import ReleaseAssetType


class ReleaseType(TypedDict):
    """Release

    A release.
    """

    url: str
    html_url: str
    assets_url: str
    upload_url: str
    tarball_url: Union[str, None]
    zipball_url: Union[str, None]
    id: int
    node_id: str
    tag_name: str
    target_commitish: str
    name: Union[str, None]
    body: NotRequired[Union[str, None]]
    draft: bool
    prerelease: bool
    created_at: datetime
    published_at: Union[datetime, None]
    author: SimpleUserType
    assets: list[ReleaseAssetType]
    body_html: NotRequired[Union[str, None]]
    body_text: NotRequired[Union[str, None]]
    mentions_count: NotRequired[int]
    discussion_url: NotRequired[str]
    reactions: NotRequired[ReactionRollupType]


__all__ = ("ReleaseType",)
