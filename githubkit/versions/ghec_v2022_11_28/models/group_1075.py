"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoGitTreesPostBody(GitHubModel):
    """ReposOwnerRepoGitTreesPostBody"""

    tree: list[ReposOwnerRepoGitTreesPostBodyPropTreeItems] = Field(
        description="Objects (of `path`, `mode`, `type`, and `sha`) specifying a tree structure."
    )
    base_tree: Missing[str] = Field(
        default=UNSET,
        description="The SHA1 of an existing Git tree object which will be used as the base for the new tree. If provided, a new Git tree object will be created from entries in the Git tree object pointed to by `base_tree` and entries defined in the `tree` parameter. Entries defined in the `tree` parameter will overwrite items from `base_tree` with the same `path`. If you're creating new changes on a branch, then normally you'd set `base_tree` to the SHA1 of the Git tree object of the current latest commit on the branch you're working on.\nIf not provided, GitHub will create a new Git tree object from only the entries defined in the `tree` parameter. If you create a new commit pointing to such a tree, then all files which were a part of the parent commit's tree and were not defined in the `tree` parameter will be listed as deleted by the new commit.",
    )


class ReposOwnerRepoGitTreesPostBodyPropTreeItems(GitHubModel):
    """ReposOwnerRepoGitTreesPostBodyPropTreeItems"""

    path: Missing[str] = Field(
        default=UNSET, description="The file referenced in the tree."
    )
    mode: Missing[Literal["100644", "100755", "040000", "160000", "120000"]] = Field(
        default=UNSET,
        description="The file mode; one of `100644` for file (blob), `100755` for executable (blob), `040000` for subdirectory (tree), `160000` for submodule (commit), or `120000` for a blob that specifies the path of a symlink.",
    )
    type: Missing[Literal["blob", "tree", "commit"]] = Field(
        default=UNSET, description="Either `blob`, `tree`, or `commit`."
    )
    sha: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The SHA1 checksum ID of the object in the tree. Also called `tree.sha`. If the value is `null` then the file will be deleted.  \n  \n**Note:** Use either `tree.sha` or `content` to specify the contents of the entry. Using both `tree.sha` and `content` will return an error.",
    )
    content: Missing[str] = Field(
        default=UNSET,
        description="The content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, or `tree.sha`.  \n  \n**Note:** Use either `tree.sha` or `content` to specify the contents of the entry. Using both `tree.sha` and `content` will return an error.",
    )


model_rebuild(ReposOwnerRepoGitTreesPostBody)
model_rebuild(ReposOwnerRepoGitTreesPostBodyPropTreeItems)

__all__ = (
    "ReposOwnerRepoGitTreesPostBody",
    "ReposOwnerRepoGitTreesPostBodyPropTreeItems",
)
