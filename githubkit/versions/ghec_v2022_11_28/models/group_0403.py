"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0398 import UserRoleItems


class User(GitHubModel):
    """User"""

    schemas: list[Literal["urn:ietf:params:scim:schemas:core:2.0:User"]] = Field(
        description="The URIs that are used to indicate the namespaces of the SCIM schemas."
    )
    external_id: str = Field(
        alias="externalId",
        description="A unique identifier for the resource as defined by the provisioning client.",
    )
    active: bool = Field(description="Whether the user active in the IdP.")
    user_name: str = Field(alias="userName", description="The username for the user.")
    name: Missing[UserName] = Field(default=UNSET)
    display_name: str = Field(
        alias="displayName", description="A human-readable name for the user."
    )
    emails: list[UserEmailsItems] = Field(description="The emails for the user.")
    roles: Missing[list[UserRoleItems]] = Field(
        default=UNSET, description="The roles assigned to the user."
    )


class UserName(GitHubModel):
    """UserName"""

    formatted: Missing[str] = Field(
        default=UNSET,
        description="The full name, including all middle names, titles, and suffixes as appropriate, formatted for display.",
    )
    family_name: str = Field(
        alias="familyName", description="The family name of the user."
    )
    given_name: str = Field(
        alias="givenName", description="The given name of the user."
    )
    middle_name: Missing[str] = Field(
        default=UNSET, alias="middleName", description="The middle name(s) of the user."
    )


class UserEmailsItems(GitHubModel):
    """UserEmailsItems"""

    value: str = Field(description="The email address.")
    type: str = Field(description="The type of email address.")
    primary: bool = Field(
        description="Whether this email address is the primary address."
    )


model_rebuild(User)
model_rebuild(UserName)
model_rebuild(UserEmailsItems)

__all__ = (
    "User",
    "UserName",
    "UserEmailsItems",
)
