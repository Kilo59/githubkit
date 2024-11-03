"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class License(GitHubModel):
    """License

    License
    """

    key: str = Field()
    name: str = Field()
    spdx_id: Union[str, None] = Field()
    url: Union[str, None] = Field()
    node_id: str = Field()
    html_url: str = Field()
    description: str = Field()
    implementation: str = Field()
    permissions: list[str] = Field()
    conditions: list[str] = Field()
    limitations: list[str] = Field()
    body: str = Field()
    featured: bool = Field()


model_rebuild(License)

__all__ = ("License",)
