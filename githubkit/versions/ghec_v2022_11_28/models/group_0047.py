"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class GetAuditLogStreamConfig(GitHubModel):
    """Get an audit log streaming configuration

    Get an audit log streaming configuration for an enterprise.
    """

    id: int = Field()
    stream_type: str = Field()
    stream_details: str = Field()
    enabled: bool = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
    paused_at: Missing[Union[datetime, None]] = Field(default=UNSET)


model_rebuild(GetAuditLogStreamConfig)

__all__ = ("GetAuditLogStreamConfig",)
