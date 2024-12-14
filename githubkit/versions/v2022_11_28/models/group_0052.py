"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0051 import SecurityAndAnalysis


class MinimalRepository(GitHubModel):
    """Minimal Repository

    Minimal Repository
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
    git_url: Missing[str] = Field(default=UNSET)
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
    ssh_url: Missing[str] = Field(default=UNSET)
    stargazers_url: str = Field()
    statuses_url: str = Field()
    subscribers_url: str = Field()
    subscription_url: str = Field()
    tags_url: str = Field()
    teams_url: str = Field()
    trees_url: str = Field()
    clone_url: Missing[str] = Field(default=UNSET)
    mirror_url: Missing[Union[str, None]] = Field(default=UNSET)
    hooks_url: str = Field()
    svn_url: Missing[str] = Field(default=UNSET)
    homepage: Missing[Union[str, None]] = Field(default=UNSET)
    language: Missing[Union[str, None]] = Field(default=UNSET)
    forks_count: Missing[int] = Field(default=UNSET)
    stargazers_count: Missing[int] = Field(default=UNSET)
    watchers_count: Missing[int] = Field(default=UNSET)
    size: Missing[int] = Field(
        default=UNSET,
        description="The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.",
    )
    default_branch: Missing[str] = Field(default=UNSET)
    open_issues_count: Missing[int] = Field(default=UNSET)
    is_template: Missing[bool] = Field(default=UNSET)
    topics: Missing[list[str]] = Field(default=UNSET)
    has_issues: Missing[bool] = Field(default=UNSET)
    has_projects: Missing[bool] = Field(default=UNSET)
    has_wiki: Missing[bool] = Field(default=UNSET)
    has_pages: Missing[bool] = Field(default=UNSET)
    has_downloads: Missing[bool] = Field(default=UNSET)
    has_discussions: Missing[bool] = Field(default=UNSET)
    archived: Missing[bool] = Field(default=UNSET)
    disabled: Missing[bool] = Field(default=UNSET)
    visibility: Missing[str] = Field(default=UNSET)
    pushed_at: Missing[Union[datetime, None]] = Field(default=UNSET)
    created_at: Missing[Union[datetime, None]] = Field(default=UNSET)
    updated_at: Missing[Union[datetime, None]] = Field(default=UNSET)
    permissions: Missing[MinimalRepositoryPropPermissions] = Field(default=UNSET)
    role_name: Missing[str] = Field(default=UNSET)
    temp_clone_token: Missing[Union[str, None]] = Field(default=UNSET)
    delete_branch_on_merge: Missing[bool] = Field(default=UNSET)
    subscribers_count: Missing[int] = Field(default=UNSET)
    network_count: Missing[int] = Field(default=UNSET)
    code_of_conduct: Missing[CodeOfConduct] = Field(
        default=UNSET, title="Code Of Conduct", description="Code Of Conduct"
    )
    license_: Missing[Union[MinimalRepositoryPropLicense, None]] = Field(
        default=UNSET, alias="license"
    )
    forks: Missing[int] = Field(default=UNSET)
    open_issues: Missing[int] = Field(default=UNSET)
    watchers: Missing[int] = Field(default=UNSET)
    allow_forking: Missing[bool] = Field(default=UNSET)
    web_commit_signoff_required: Missing[bool] = Field(default=UNSET)
    security_and_analysis: Missing[Union[SecurityAndAnalysis, None]] = Field(
        default=UNSET
    )


class CodeOfConduct(GitHubModel):
    """Code Of Conduct

    Code Of Conduct
    """

    key: str = Field()
    name: str = Field()
    url: str = Field()
    body: Missing[str] = Field(default=UNSET)
    html_url: Union[str, None] = Field()


class MinimalRepositoryPropPermissions(GitHubModel):
    """MinimalRepositoryPropPermissions"""

    admin: Missing[bool] = Field(default=UNSET)
    maintain: Missing[bool] = Field(default=UNSET)
    push: Missing[bool] = Field(default=UNSET)
    triage: Missing[bool] = Field(default=UNSET)
    pull: Missing[bool] = Field(default=UNSET)


class MinimalRepositoryPropLicense(GitHubModel):
    """MinimalRepositoryPropLicense"""

    key: Missing[str] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    spdx_id: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)


model_rebuild(MinimalRepository)
model_rebuild(CodeOfConduct)
model_rebuild(MinimalRepositoryPropPermissions)
model_rebuild(MinimalRepositoryPropLicense)

__all__ = (
    "CodeOfConduct",
    "MinimalRepository",
    "MinimalRepositoryPropLicense",
    "MinimalRepositoryPropPermissions",
)
