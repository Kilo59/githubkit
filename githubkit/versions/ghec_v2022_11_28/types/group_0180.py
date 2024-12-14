"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict


class OrganizationCustomOrganizationRoleCreateSchemaType(TypedDict):
    """OrganizationCustomOrganizationRoleCreateSchema"""

    name: str
    description: NotRequired[str]
    permissions: list[str]
    base_role: NotRequired[Literal["read", "triage", "write", "maintain", "admin"]]


__all__ = ("OrganizationCustomOrganizationRoleCreateSchemaType",)
