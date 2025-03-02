"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0055 import CodeScanningAlertRuleSummaryType
from .group_0056 import CodeScanningAnalysisToolType
from .group_0057 import CodeScanningAlertInstanceType
from .group_0058 import SimpleRepositoryType


class CodeScanningOrganizationAlertItemsType(TypedDict):
    """CodeScanningOrganizationAlertItems"""

    number: int
    created_at: datetime
    updated_at: NotRequired[datetime]
    url: str
    html_url: str
    instances_url: str
    state: Union[None, Literal["open", "dismissed", "fixed"]]
    fixed_at: NotRequired[Union[datetime, None]]
    dismissed_by: Union[None, SimpleUserType]
    dismissed_at: Union[datetime, None]
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ]
    dismissed_comment: NotRequired[Union[str, None]]
    rule: CodeScanningAlertRuleSummaryType
    tool: CodeScanningAnalysisToolType
    most_recent_instance: CodeScanningAlertInstanceType
    repository: SimpleRepositoryType
    dismissal_approved_by: NotRequired[Union[None, SimpleUserType]]


__all__ = ("CodeScanningOrganizationAlertItemsType",)
