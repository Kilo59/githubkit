"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class ReposOwnerRepoImportPatchBodyType(TypedDict):
    """ReposOwnerRepoImportPatchBody"""

    vcs_username: NotRequired[str]
    vcs_password: NotRequired[str]
    vcs: NotRequired[Literal["subversion", "tfvc", "git", "mercurial"]]
    tfvc_project: NotRequired[str]


__all__ = ("ReposOwnerRepoImportPatchBodyType",)
