"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0248 import Link


class ReviewCommentPropLinks(GitHubModel):
    """ReviewCommentPropLinks"""

    self_: Link = Field(alias="self", title="Link", description="Hypermedia Link")
    html: Link = Field(title="Link", description="Hypermedia Link")
    pull_request: Link = Field(title="Link", description="Hypermedia Link")


model_rebuild(ReviewCommentPropLinks)

__all__ = ("ReviewCommentPropLinks",)
