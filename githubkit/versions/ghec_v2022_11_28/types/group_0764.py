"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0439 import EnterpriseWebhooksType
from .group_0440 import SimpleInstallationType
from .group_0441 import OrganizationSimpleWebhooksType
from .group_0442 import RepositoryWebhooksType


class WebhookRepositoryEditedType(TypedDict):
    """repository edited event"""

    action: Literal["edited"]
    changes: WebhookRepositoryEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookRepositoryEditedPropChangesType(TypedDict):
    """WebhookRepositoryEditedPropChanges"""

    default_branch: NotRequired[WebhookRepositoryEditedPropChangesPropDefaultBranchType]
    description: NotRequired[WebhookRepositoryEditedPropChangesPropDescriptionType]
    homepage: NotRequired[WebhookRepositoryEditedPropChangesPropHomepageType]
    topics: NotRequired[WebhookRepositoryEditedPropChangesPropTopicsType]


class WebhookRepositoryEditedPropChangesPropDefaultBranchType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropDefaultBranch"""

    from_: str


class WebhookRepositoryEditedPropChangesPropDescriptionType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropDescription"""

    from_: Union[str, None]


class WebhookRepositoryEditedPropChangesPropHomepageType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropHomepage"""

    from_: Union[str, None]


class WebhookRepositoryEditedPropChangesPropTopicsType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropTopics"""

    from_: NotRequired[Union[list[str], None]]


__all__ = (
    "WebhookRepositoryEditedPropChangesPropDefaultBranchType",
    "WebhookRepositoryEditedPropChangesPropDescriptionType",
    "WebhookRepositoryEditedPropChangesPropHomepageType",
    "WebhookRepositoryEditedPropChangesPropTopicsType",
    "WebhookRepositoryEditedPropChangesType",
    "WebhookRepositoryEditedType",
)
