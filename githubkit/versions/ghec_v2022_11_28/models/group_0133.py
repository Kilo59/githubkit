"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0002 import SimpleUser
from .group_0019 import Repository
from .group_0018 import LicenseSimple
from .group_0084 import SecurityAndAnalysis
from .group_0132 import CodeOfConductSimple


class FullRepository(GitHubModel):
    """Full Repository

    Full Repository
    """

    id: int = Field()
    node_id: str = Field()
    name: str = Field()
    full_name: str = Field()
    owner: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    private: bool = Field()
    html_url: str = Field()
    description: Union[str, None] = Field()
    fork: bool = Field()
    url: str = Field()
    archive_url: str = Field()
    assignees_url: str = Field()
    blobs_url: str = Field()
    branches_url: str = Field()
    collaborators_url: str = Field()
    comments_url: str = Field()
    commits_url: str = Field()
    compare_url: str = Field()
    contents_url: str = Field()
    contributors_url: str = Field()
    deployments_url: str = Field()
    downloads_url: str = Field()
    events_url: str = Field()
    forks_url: str = Field()
    git_commits_url: str = Field()
    git_refs_url: str = Field()
    git_tags_url: str = Field()
    git_url: str = Field()
    issue_comment_url: str = Field()
    issue_events_url: str = Field()
    issues_url: str = Field()
    keys_url: str = Field()
    labels_url: str = Field()
    languages_url: str = Field()
    merges_url: str = Field()
    milestones_url: str = Field()
    notifications_url: str = Field()
    pulls_url: str = Field()
    releases_url: str = Field()
    ssh_url: str = Field()
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    clone_url: str = Field()
    mirror_url: Union[str, None] = Field()
    hooks_url: str = Field()
    svn_url: str = Field()
    homepage: Union[str, None] = Field()
    language: Union[str, None] = Field()
    forks_count: int = Field()
    stargazers_count: int = Field()
    watchers_count: int = Field()
    size: int = Field(
        description="The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0."
    )
    default_branch: str = Field()
    open_issues_count: int = Field()
    is_template: Missing[bool] = Field(default=UNSET)
    topics: Missing[list[str]] = Field(default=UNSET)
    has_issues: bool = Field()
    has_projects: bool = Field()
    has_wiki: bool = Field()
    has_pages: bool = Field()
    has_downloads: Missing[bool] = Field(default=UNSET)
    has_discussions: bool = Field()
    archived: bool = Field()
    disabled: bool = Field(
        description="Returns whether or not this repository disabled."
    )
    visibility: Missing[str] = Field(
        default=UNSET,
        description="The repository visibility: public, private, or internal.",
    )
    pushed_at: datetime = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    permissions: Missing[FullRepositoryPropPermissions] = Field(default=UNSET)
    allow_rebase_merge: Missing[bool] = Field(default=UNSET)
    template_repository: Missing[Union[None, Repository]] = Field(default=UNSET)
    temp_clone_token: Missing[Union[str, None]] = Field(default=UNSET)
    allow_squash_merge: Missing[bool] = Field(default=UNSET)
    allow_auto_merge: Missing[bool] = Field(default=UNSET)
    delete_branch_on_merge: Missing[bool] = Field(default=UNSET)
    allow_merge_commit: Missing[bool] = Field(default=UNSET)
    allow_update_branch: Missing[bool] = Field(default=UNSET)
    use_squash_pr_title_as_default: Missing[bool] = Field(default=UNSET)
    squash_merge_commit_title: Missing[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]] = (
        Field(
            default=UNSET,
            description="The default value for a squash merge commit title:\n\n- `PR_TITLE` - default to the pull request's title.\n- `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).",
        )
    )
    squash_merge_commit_message: Missing[
        Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    ] = Field(
        default=UNSET,
        description="The default value for a squash merge commit message:\n\n- `PR_BODY` - default to the pull request's body.\n- `COMMIT_MESSAGES` - default to the branch's commit messages.\n- `BLANK` - default to a blank commit message.",
    )
    merge_commit_title: Missing[Literal["PR_TITLE", "MERGE_MESSAGE"]] = Field(
        default=UNSET,
        description="The default value for a merge commit title.\n\n  - `PR_TITLE` - default to the pull request's title.\n  - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).",
    )
    merge_commit_message: Missing[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = Field(
        default=UNSET,
        description="The default value for a merge commit message.\n\n- `PR_TITLE` - default to the pull request's title.\n- `PR_BODY` - default to the pull request's body.\n- `BLANK` - default to a blank commit message.",
    )
    allow_forking: Missing[bool] = Field(default=UNSET)
    web_commit_signoff_required: Missing[bool] = Field(default=UNSET)
    subscribers_count: int = Field()
    network_count: int = Field()
    license_: Union[None, LicenseSimple] = Field(alias="license")
    organization: Missing[Union[None, SimpleUser]] = Field(default=UNSET)
    parent: Missing[Repository] = Field(
        default=UNSET, title="Repository", description="A repository on GitHub."
    )
    source: Missing[Repository] = Field(
        default=UNSET, title="Repository", description="A repository on GitHub."
    )
    forks: int = Field()
    master_branch: Missing[str] = Field(default=UNSET)
    open_issues: int = Field()
    watchers: int = Field()
    anonymous_access_enabled: Missing[bool] = Field(
        default=UNSET, description="Whether anonymous git access is allowed."
    )
    code_of_conduct: Missing[CodeOfConductSimple] = Field(
        default=UNSET,
        title="Code Of Conduct Simple",
        description="Code of Conduct Simple",
    )
    security_and_analysis: Missing[Union[SecurityAndAnalysis, None]] = Field(
        default=UNSET
    )
    custom_properties: Missing[FullRepositoryPropCustomProperties] = Field(
        default=UNSET,
        description="The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.",
    )


class FullRepositoryPropPermissions(GitHubModel):
    """FullRepositoryPropPermissions"""

    admin: bool = Field()
    maintain: Missing[bool] = Field(default=UNSET)
    push: bool = Field()
    triage: Missing[bool] = Field(default=UNSET)
    pull: bool = Field()


class FullRepositoryPropCustomProperties(ExtraGitHubModel):
    """FullRepositoryPropCustomProperties

    The custom properties that were defined for the repository. The keys are the
    custom property names, and the values are the corresponding custom property
    values.
    """


model_rebuild(FullRepository)
model_rebuild(FullRepositoryPropPermissions)
model_rebuild(FullRepositoryPropCustomProperties)

__all__ = (
    "FullRepository",
    "FullRepositoryPropPermissions",
    "FullRepositoryPropCustomProperties",
)
