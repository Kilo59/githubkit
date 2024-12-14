"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET


class ReposOwnerRepoGitTagsPostBody(GitHubModel):
    """ReposOwnerRepoGitTagsPostBody"""

    tag: str = Field(
        description='The tag\'s name. This is typically a version (e.g., "v0.0.1").'
    )
    message: str = Field(description="The tag message.")
    object_: str = Field(
        alias="object", description="The SHA of the git object this is tagging."
    )
    type: Literal["commit", "tree", "blob"] = Field(
        description="The type of the object we're tagging. Normally this is a `commit` but it can also be a `tree` or a `blob`."
    )
    tagger: Missing[ReposOwnerRepoGitTagsPostBodyPropTagger] = Field(
        default=UNSET,
        description="An object with information about the individual creating the tag.",
    )


class ReposOwnerRepoGitTagsPostBodyPropTagger(GitHubModel):
    """ReposOwnerRepoGitTagsPostBodyPropTagger

    An object with information about the individual creating the tag.
    """

    name: str = Field(description="The name of the author of the tag")
    email: str = Field(description="The email of the author of the tag")
    date: Missing[datetime] = Field(
        default=UNSET,
        description="When this object was tagged. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )


model_rebuild(ReposOwnerRepoGitTagsPostBody)
model_rebuild(ReposOwnerRepoGitTagsPostBodyPropTagger)

__all__ = (
    "ReposOwnerRepoGitTagsPostBody",
    "ReposOwnerRepoGitTagsPostBodyPropTagger",
)
