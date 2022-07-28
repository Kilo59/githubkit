"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .models import (
    ScimUser,
    ScimError,
    BasicError,
    ScimUserList,
    ScimV2OrganizationsOrgUsersPostBody,
    ScimV2OrganizationsOrgUsersScimUserIdPutBody,
    ScimV2OrganizationsOrgUsersScimUserIdPatchBody,
)
from .types import (
    ScimV2OrganizationsOrgUsersPostBodyType,
    ScimV2OrganizationsOrgUsersPostBodyPropNameType,
    ScimV2OrganizationsOrgUsersScimUserIdPutBodyType,
    ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType,
    ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType,
    ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType,
    ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType,
    ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsType,
)

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


class ScimClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_provisioned_identities(
        self,
        org: str,
        start_index: Union[Unset, int] = UNSET,
        count: Union[Unset, int] = UNSET,
        filter_: Union[Unset, str] = UNSET,
    ) -> "Response[ScimUserList]":
        url = f"/scim/v2/organizations/{org}/Users"

        params = {
            "startIndex": start_index,
            "count": count,
            "filter": filter_,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ScimUserList,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": ScimError,
            },
        )

    async def async_list_provisioned_identities(
        self,
        org: str,
        start_index: Union[Unset, int] = UNSET,
        count: Union[Unset, int] = UNSET,
        filter_: Union[Unset, str] = UNSET,
    ) -> "Response[ScimUserList]":
        url = f"/scim/v2/organizations/{org}/Users"

        params = {
            "startIndex": start_index,
            "count": count,
            "filter": filter_,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ScimUserList,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": ScimError,
            },
        )

    @overload
    def provision_and_invite_user(
        self, org: str, *, data: ScimV2OrganizationsOrgUsersPostBodyType
    ) -> "Response[ScimUser]":
        ...

    @overload
    def provision_and_invite_user(
        self,
        org: str,
        *,
        data: Unset = UNSET,
        user_name: str,
        display_name: Union[Unset, str] = UNSET,
        name: ScimV2OrganizationsOrgUsersPostBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType],
        schemas: Union[Unset, List[str]] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
    ) -> "Response[ScimUser]":
        ...

    def provision_and_invite_user(
        self,
        org: str,
        *,
        data: Union[Unset, ScimV2OrganizationsOrgUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ScimV2OrganizationsOrgUsersPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "500": ScimError,
                "409": ScimError,
                "400": ScimError,
            },
        )

    @overload
    async def async_provision_and_invite_user(
        self, org: str, *, data: ScimV2OrganizationsOrgUsersPostBodyType
    ) -> "Response[ScimUser]":
        ...

    @overload
    async def async_provision_and_invite_user(
        self,
        org: str,
        *,
        data: Unset = UNSET,
        user_name: str,
        display_name: Union[Unset, str] = UNSET,
        name: ScimV2OrganizationsOrgUsersPostBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersPostBodyPropEmailsItemsType],
        schemas: Union[Unset, List[str]] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
    ) -> "Response[ScimUser]":
        ...

    async def async_provision_and_invite_user(
        self,
        org: str,
        *,
        data: Union[Unset, ScimV2OrganizationsOrgUsersPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ScimV2OrganizationsOrgUsersPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "500": ScimError,
                "409": ScimError,
                "400": ScimError,
            },
        )

    def get_provisioning_information_for_user(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return self._github.request(
            "GET",
            url,
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    async def async_get_provisioning_information_for_user(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    @overload
    def set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: ScimV2OrganizationsOrgUsersScimUserIdPutBodyType,
    ) -> "Response[ScimUser]":
        ...

    @overload
    def set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Unset = UNSET,
        schemas: Union[Unset, List[str]] = UNSET,
        display_name: Union[Unset, str] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
        user_name: str,
        name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType],
    ) -> "Response[ScimUser]":
        ...

    def set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Union[Unset, ScimV2OrganizationsOrgUsersScimUserIdPutBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ScimV2OrganizationsOrgUsersScimUserIdPutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    @overload
    async def async_set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: ScimV2OrganizationsOrgUsersScimUserIdPutBodyType,
    ) -> "Response[ScimUser]":
        ...

    @overload
    async def async_set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Unset = UNSET,
        schemas: Union[Unset, List[str]] = UNSET,
        display_name: Union[Unset, str] = UNSET,
        external_id: Union[Unset, str] = UNSET,
        groups: Union[Unset, List[str]] = UNSET,
        active: Union[Unset, bool] = UNSET,
        user_name: str,
        name: ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropNameType,
        emails: List[ScimV2OrganizationsOrgUsersScimUserIdPutBodyPropEmailsItemsType],
    ) -> "Response[ScimUser]":
        ...

    async def async_set_information_for_provisioned_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Union[Unset, ScimV2OrganizationsOrgUsersScimUserIdPutBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ScimV2OrganizationsOrgUsersScimUserIdPutBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    def delete_user_from_org(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return self._github.request(
            "DELETE",
            url,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    async def async_delete_user_from_org(
        self,
        org: str,
        scim_user_id: str,
    ) -> "Response":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        return await self._github.arequest(
            "DELETE",
            url,
            error_models={
                "404": ScimError,
                "403": ScimError,
            },
        )

    @overload
    def update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType,
    ) -> "Response[ScimUser]":
        ...

    @overload
    def update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Unset = UNSET,
        schemas: Union[Unset, List[str]] = UNSET,
        operations: List[
            ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsType
        ],
    ) -> "Response[ScimUser]":
        ...

    def update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Union[Unset, ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ScimV2OrganizationsOrgUsersScimUserIdPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": BasicError,
            },
        )

    @overload
    async def async_update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType,
    ) -> "Response[ScimUser]":
        ...

    @overload
    async def async_update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Unset = UNSET,
        schemas: Union[Unset, List[str]] = UNSET,
        operations: List[
            ScimV2OrganizationsOrgUsersScimUserIdPatchBodyPropOperationsItemsType
        ],
    ) -> "Response[ScimUser]":
        ...

    async def async_update_attribute_for_user(
        self,
        org: str,
        scim_user_id: str,
        *,
        data: Union[Unset, ScimV2OrganizationsOrgUsersScimUserIdPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[ScimUser]":
        url = f"/scim/v2/organizations/{org}/Users/{scim_user_id}"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ScimV2OrganizationsOrgUsersScimUserIdPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            response_model=ScimUser,
            error_models={
                "404": ScimError,
                "403": ScimError,
                "400": ScimError,
                "429": BasicError,
            },
        )
