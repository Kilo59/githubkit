"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .models import License, BasicError, LicenseSimple, LicenseContent

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


class LicensesClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_all_commonly_used(
        self,
        featured: Union[Unset, bool] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[LicenseSimple]]":
        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[LicenseSimple],
        )

    async def async_get_all_commonly_used(
        self,
        featured: Union[Unset, bool] = UNSET,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[List[LicenseSimple]]":
        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[LicenseSimple],
        )

    def get(
        self,
        license_: str,
    ) -> "Response[License]":
        url = f"/licenses/{license}"

        return self._github.request(
            "GET",
            url,
            response_model=License,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get(
        self,
        license_: str,
    ) -> "Response[License]":
        url = f"/licenses/{license}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=License,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    def get_for_repo(
        self,
        owner: str,
        repo: str,
    ) -> "Response[LicenseContent]":
        url = f"/repos/{owner}/{repo}/license"

        return self._github.request(
            "GET",
            url,
            response_model=LicenseContent,
        )

    async def async_get_for_repo(
        self,
        owner: str,
        repo: str,
    ) -> "Response[LicenseContent]":
        url = f"/repos/{owner}/{repo}/license"

        return await self._github.arequest(
            "GET",
            url,
            response_model=LicenseContent,
        )
