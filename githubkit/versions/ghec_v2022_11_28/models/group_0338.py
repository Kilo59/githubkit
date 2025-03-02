"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0003 import SimpleUser
from .group_0010 import Integration


class LabeledIssueEvent(GitHubModel):
    """Labeled Issue Event

    Labeled Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["labeled"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration, None] = Field()
    label: LabeledIssueEventPropLabel = Field()


class LabeledIssueEventPropLabel(GitHubModel):
    """LabeledIssueEventPropLabel"""

    name: str = Field()
    color: str = Field()


model_rebuild(LabeledIssueEvent)
model_rebuild(LabeledIssueEventPropLabel)

__all__ = (
    "LabeledIssueEvent",
    "LabeledIssueEventPropLabel",
)
