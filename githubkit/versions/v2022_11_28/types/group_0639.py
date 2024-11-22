"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0002 import SimpleUserType
from .group_0420 import ProjectsV2ItemType
from .group_0385 import SimpleInstallationType
from .group_0386 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ItemDeletedType(TypedDict):
    """Projects v2 Item Deleted Event"""

    action: Literal["deleted"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2_item: ProjectsV2ItemType
    sender: SimpleUserType


__all__ = ("WebhookProjectsV2ItemDeletedType",)
