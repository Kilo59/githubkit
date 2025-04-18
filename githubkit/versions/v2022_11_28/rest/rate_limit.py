"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Optional
from weakref import ref

from githubkit.utils import exclude_unset

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response

    from ..models import RateLimitOverview
    from ..types import RateLimitOverviewType


class RateLimitClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    def get(
        self,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[RateLimitOverview, RateLimitOverviewType]:
        """See also: https://docs.github.com/rest/rate-limit/rate-limit#get-rate-limit-status-for-the-authenticated-user"""

        from ..models import BasicError, RateLimitOverview

        url = "/rate_limit"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=RateLimitOverview,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get(
        self,
        *,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Response[RateLimitOverview, RateLimitOverviewType]:
        """See also: https://docs.github.com/rest/rate-limit/rate-limit#get-rate-limit-status-for-the-authenticated-user"""

        from ..models import BasicError, RateLimitOverview

        url = "/rate_limit"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=RateLimitOverview,
            error_models={
                "404": BasicError,
            },
        )
