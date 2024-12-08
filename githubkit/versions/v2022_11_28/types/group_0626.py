"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal, Union
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0388 import EnterpriseWebhooksType
from .group_0389 import SimpleInstallationType
from .group_0390 import OrganizationSimpleWebhooksType
from .group_0391 import RepositoryWebhooksType
from .group_0419 import WebhooksProjectCardType


class WebhookProjectCardEditedType(TypedDict):
    """project_card edited event"""

    action: Literal["edited"]
    changes: WebhookProjectCardEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project_card: WebhooksProjectCardType
    repository: NotRequired[RepositoryWebhooksType]
    sender: SimpleUserType


class WebhookProjectCardEditedPropChangesType(TypedDict):
    """WebhookProjectCardEditedPropChanges"""

    note: WebhookProjectCardEditedPropChangesPropNoteType


class WebhookProjectCardEditedPropChangesPropNoteType(TypedDict):
    """WebhookProjectCardEditedPropChangesPropNote"""

    from_: Union[str, None]


__all__ = (
    "WebhookProjectCardEditedPropChangesPropNoteType",
    "WebhookProjectCardEditedPropChangesType",
    "WebhookProjectCardEditedType",
)
