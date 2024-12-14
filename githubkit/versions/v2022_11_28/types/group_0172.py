"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0171 import RateLimitType
from .group_0173 import RateLimitOverviewPropResourcesType


class RateLimitOverviewType(TypedDict):
    """Rate Limit Overview

    Rate Limit Overview
    """

    resources: RateLimitOverviewPropResourcesType
    rate: RateLimitType


__all__ = ("RateLimitOverviewType",)
