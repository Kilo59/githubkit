"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0003 import SimpleUserType
from .group_0458 import EnterpriseWebhooksType
from .group_0459 import SimpleInstallationType
from .group_0460 import OrganizationSimpleWebhooksType
from .group_0461 import RepositoryWebhooksType
from .group_0473 import DiscussionType


class WebhookDiscussionCategoryChangedType(TypedDict):
    """discussion category changed event"""

    action: Literal["category_changed"]
    changes: WebhookDiscussionCategoryChangedPropChangesType
    discussion: DiscussionType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookDiscussionCategoryChangedPropChangesType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChanges"""

    category: WebhookDiscussionCategoryChangedPropChangesPropCategoryType


class WebhookDiscussionCategoryChangedPropChangesPropCategoryType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChangesPropCategory"""

    from_: WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType


class WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType(TypedDict):
    """WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFrom"""

    created_at: datetime
    description: str
    emoji: str
    id: int
    is_answerable: bool
    name: str
    node_id: NotRequired[str]
    repository_id: int
    slug: str
    updated_at: str


__all__ = (
    "WebhookDiscussionCategoryChangedPropChangesPropCategoryPropFromType",
    "WebhookDiscussionCategoryChangedPropChangesPropCategoryType",
    "WebhookDiscussionCategoryChangedPropChangesType",
    "WebhookDiscussionCategoryChangedType",
)
