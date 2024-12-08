"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0388 import EnterpriseWebhooksType
from .group_0389 import SimpleInstallationType
from .group_0390 import OrganizationSimpleWebhooksType
from .group_0391 import RepositoryWebhooksType


class WebhookProjectCardMovedType(TypedDict):
    """project_card moved event"""

    action: Literal["moved"]
    changes: NotRequired[WebhookProjectCardMovedPropChangesType]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_card: WebhookProjectCardMovedPropProjectCardType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


class WebhookProjectCardMovedPropChangesType(TypedDict):
    """WebhookProjectCardMovedPropChanges"""

    column_id: WebhookProjectCardMovedPropChangesPropColumnIdType


class WebhookProjectCardMovedPropChangesPropColumnIdType(TypedDict):
    """WebhookProjectCardMovedPropChangesPropColumnId"""

    from_: int


class WebhookProjectCardMovedPropProjectCardType(TypedDict):
    """WebhookProjectCardMovedPropProjectCard"""

    after_id: Union[Union[int, None], None]
    archived: bool
    column_id: int
    column_url: str
    content_url: NotRequired[str]
    created_at: datetime
    creator: Union[WebhookProjectCardMovedPropProjectCardMergedCreatorType, None]
    id: int
    node_id: str
    note: Union[Union[str, None], None]
    project_url: str
    updated_at: datetime
    url: str


class WebhookProjectCardMovedPropProjectCardMergedCreatorType(TypedDict):
    """WebhookProjectCardMovedPropProjectCardMergedCreator"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization", "Mannequin"]]
    url: NotRequired[str]
    user_view_type: NotRequired[str]


__all__ = (
    "WebhookProjectCardMovedPropChangesPropColumnIdType",
    "WebhookProjectCardMovedPropChangesType",
    "WebhookProjectCardMovedPropProjectCardMergedCreatorType",
    "WebhookProjectCardMovedPropProjectCardType",
    "WebhookProjectCardMovedType",
)
