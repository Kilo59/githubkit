"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0161 import MinimalRepositoryType


class PackageType(TypedDict):
    """Package

    A software package
    """

    id: int
    name: str
    package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"]
    url: str
    html_url: str
    version_count: int
    visibility: Literal["private", "public"]
    owner: NotRequired[Union[None, SimpleUserType]]
    repository: NotRequired[Union[None, MinimalRepositoryType]]
    created_at: datetime
    updated_at: datetime


__all__ = ("PackageType",)
