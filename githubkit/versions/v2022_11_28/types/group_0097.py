"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import NotRequired, TypedDict


class ApiInsightsSubjectStatsItemsType(TypedDict):
    """ApiInsightsSubjectStatsItems"""

    subject_type: NotRequired[str]
    subject_name: NotRequired[str]
    subject_id: NotRequired[int]
    total_request_count: NotRequired[int]
    rate_limited_request_count: NotRequired[int]
    last_rate_limited_timestamp: NotRequired[Union[str, None]]
    last_request_timestamp: NotRequired[str]


__all__ = ("ApiInsightsSubjectStatsItemsType",)
