"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ScimUserList(GitHubModel):
    """SCIM User List

    SCIM User List
    """

    schemas: List[str] = Field(min_length=1, description="SCIM schema used.")
    total_results: int = Field(alias="totalResults")
    items_per_page: int = Field(alias="itemsPerPage")
    start_index: int = Field(alias="startIndex")
    resources: List[ScimUser] = Field(alias="Resources")


class ScimUser(GitHubModel):
    """SCIM /Users

    SCIM /Users provisioning endpoints
    """

    schemas: List[str] = Field(min_length=1, description="SCIM schema used.")
    id: str = Field(description="Unique identifier of an external identity")
    external_id: Missing[Union[str, None]] = Field(
        default=UNSET, alias="externalId", description="The ID of the User."
    )
    user_name: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="userName",
        description="Configured by the admin. Could be an email, login, or username",
    )
    display_name: Missing[Union[str, None]] = Field(
        default=UNSET,
        alias="displayName",
        description="The name of the user, suitable for display to end-users",
    )
    name: Missing[ScimUserPropName] = Field(default=UNSET)
    emails: List[ScimUserPropEmailsItems] = Field(description="user emails")
    active: bool = Field(description="The active status of the User.")
    meta: ScimUserPropMeta = Field()
    organization_id: Missing[int] = Field(
        default=UNSET, description="The ID of the organization."
    )
    operations: Missing[List[ScimUserPropOperationsItems]] = Field(
        min_length=1, default=UNSET, description="Set of operations to be performed"
    )
    groups: Missing[List[ScimUserPropGroupsItems]] = Field(
        default=UNSET, description="associated groups"
    )
    roles: Missing[List[ScimUserPropRolesItems]] = Field(default=UNSET)


class ScimUserPropName(GitHubModel):
    """ScimUserPropName

    Examples:
        {'givenName': 'Jane', 'familyName': 'User'}
    """

    given_name: Missing[Union[str, None]] = Field(default=UNSET, alias="givenName")
    family_name: Missing[Union[str, None]] = Field(default=UNSET, alias="familyName")
    formatted: Missing[Union[str, None]] = Field(default=UNSET)


class ScimUserPropEmailsItems(GitHubModel):
    """ScimUserPropEmailsItems"""

    value: str = Field()
    primary: Missing[bool] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)


class ScimUserPropMeta(GitHubModel):
    """ScimUserPropMeta"""

    resource_type: Missing[str] = Field(default=UNSET, alias="resourceType")
    created: Missing[datetime] = Field(default=UNSET)
    last_modified: Missing[datetime] = Field(default=UNSET, alias="lastModified")
    location: Missing[str] = Field(default=UNSET)


class ScimUserPropGroupsItems(GitHubModel):
    """ScimUserPropGroupsItems"""

    value: Missing[str] = Field(default=UNSET)
    display: Missing[str] = Field(default=UNSET)


class ScimUserPropRolesItems(GitHubModel):
    """ScimUserPropRolesItems"""

    value: Missing[str] = Field(default=UNSET)
    primary: Missing[bool] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    display: Missing[str] = Field(default=UNSET)


class ScimUserPropOperationsItems(GitHubModel):
    """ScimUserPropOperationsItems"""

    op: Literal["add", "remove", "replace"] = Field()
    path: Missing[str] = Field(default=UNSET)
    value: Missing[
        Union[str, ScimUserPropOperationsItemsPropValueOneof1, List[Any]]
    ] = Field(default=UNSET)


class ScimUserPropOperationsItemsPropValueOneof1(GitHubModel):
    """ScimUserPropOperationsItemsPropValueOneof1"""


model_rebuild(ScimUserList)
model_rebuild(ScimUser)
model_rebuild(ScimUserPropName)
model_rebuild(ScimUserPropEmailsItems)
model_rebuild(ScimUserPropMeta)
model_rebuild(ScimUserPropGroupsItems)
model_rebuild(ScimUserPropRolesItems)
model_rebuild(ScimUserPropOperationsItems)
model_rebuild(ScimUserPropOperationsItemsPropValueOneof1)

__all__ = (
    "ScimUserList",
    "ScimUser",
    "ScimUserPropName",
    "ScimUserPropEmailsItems",
    "ScimUserPropMeta",
    "ScimUserPropGroupsItems",
    "ScimUserPropRolesItems",
    "ScimUserPropOperationsItems",
    "ScimUserPropOperationsItemsPropValueOneof1",
)
