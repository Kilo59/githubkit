"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0413 import ProjectsV2ItemType
from .group_0377 import SimpleInstallationType
from .group_0380 import SimpleUserWebhooksType
from .group_0412 import WebhooksProjectChangesType
from .group_0378 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemArchivedType(TypedDict):
    """Projects v2 Item Archived Event"""

    action: Literal["archived"]
    changes: WebhooksProjectChangesType
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserWebhooksType


__all__ = ("WebhookProjectsV2ItemArchivedType",)
