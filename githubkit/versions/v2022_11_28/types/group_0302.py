"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class PageDeploymentType(TypedDict):
    """GitHub Pages

    The GitHub Pages deployment status.
    """

    id: Union[int, str]
    status_url: str
    page_url: str
    preview_url: NotRequired[str]


__all__ = ("PageDeploymentType",)
