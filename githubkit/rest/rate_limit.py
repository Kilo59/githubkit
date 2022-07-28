"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import exclude_unset

from .models import BasicError, RateLimitOverview

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


class RateLimitClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get(
        self,
    ) -> "Response[RateLimitOverview]":
        url = "/rate_limit"

        return self._github.request(
            "GET",
            url,
            response_model=RateLimitOverview,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get(
        self,
    ) -> "Response[RateLimitOverview]":
        url = "/rate_limit"

        return await self._github.arequest(
            "GET",
            url,
            response_model=RateLimitOverview,
            error_models={
                "404": BasicError,
            },
        )
