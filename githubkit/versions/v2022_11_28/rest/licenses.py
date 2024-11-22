"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from weakref import ref
from typing import TYPE_CHECKING, Optional

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import License, LicenseSimple, LicenseContent
    from ..types import LicenseType, LicenseSimpleType, LicenseContentType


class LicensesClient:
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

    def get_all_commonly_used(
        self,
        *,
        featured: Missing[bool] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[list[LicenseSimple], list[LicenseSimpleType]]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-all-commonly-used-licenses"""

        from ..models import LicenseSimple

        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=list[LicenseSimple],
        )

    async def async_get_all_commonly_used(
        self,
        *,
        featured: Missing[bool] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[list[LicenseSimple], list[LicenseSimpleType]]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-all-commonly-used-licenses"""

        from ..models import LicenseSimple

        url = "/licenses"

        params = {
            "featured": featured,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=list[LicenseSimple],
        )

    def get(
        self,
        license_: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[License, LicenseType]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-a-license"""

        from ..models import License, BasicError

        url = f"/licenses/{license}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=License,
            error_models={
                "403": BasicError,
                "404": BasicError,
            },
        )

    async def async_get(
        self,
        license_: str,
        *,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[License, LicenseType]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-a-license"""

        from ..models import License, BasicError

        url = f"/licenses/{license}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
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
        *,
        ref: Missing[str] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[LicenseContent, LicenseContentType]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository"""

        from ..models import BasicError, LicenseContent

        url = f"/repos/{owner}/{repo}/license"

        params = {
            "ref": ref,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=LicenseContent,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        ref: Missing[str] = UNSET,
        headers: Optional[dict[str, str]] = None,
    ) -> Response[LicenseContent, LicenseContentType]:
        """See also: https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository"""

        from ..models import BasicError, LicenseContent

        url = f"/repos/{owner}/{repo}/license"

        params = {
            "ref": ref,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=LicenseContent,
            error_models={
                "404": BasicError,
            },
        )
