"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import NotRequired, TypedDict

from .group_0002 import SimpleUserType
from .group_0439 import EnterpriseWebhooksType
from .group_0440 import SimpleInstallationType
from .group_0441 import OrganizationSimpleWebhooksType
from .group_0442 import RepositoryWebhooksType
from .group_0462 import WebhooksMilestoneType


class WebhookMilestoneEditedType(TypedDict):
    """milestone edited event"""

    action: Literal["edited"]
    changes: WebhookMilestoneEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    milestone: WebhooksMilestoneType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserType


class WebhookMilestoneEditedPropChangesType(TypedDict):
    """WebhookMilestoneEditedPropChanges

    The changes to the milestone if the action was `edited`.
    """

    description: NotRequired[WebhookMilestoneEditedPropChangesPropDescriptionType]
    due_on: NotRequired[WebhookMilestoneEditedPropChangesPropDueOnType]
    title: NotRequired[WebhookMilestoneEditedPropChangesPropTitleType]


class WebhookMilestoneEditedPropChangesPropDescriptionType(TypedDict):
    """WebhookMilestoneEditedPropChangesPropDescription"""

    from_: str


class WebhookMilestoneEditedPropChangesPropDueOnType(TypedDict):
    """WebhookMilestoneEditedPropChangesPropDueOn"""

    from_: str


class WebhookMilestoneEditedPropChangesPropTitleType(TypedDict):
    """WebhookMilestoneEditedPropChangesPropTitle"""

    from_: str


__all__ = (
    "WebhookMilestoneEditedPropChangesPropDescriptionType",
    "WebhookMilestoneEditedPropChangesPropDueOnType",
    "WebhookMilestoneEditedPropChangesPropTitleType",
    "WebhookMilestoneEditedPropChangesType",
    "WebhookMilestoneEditedType",
)
