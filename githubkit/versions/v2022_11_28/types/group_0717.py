"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from .group_0113 import RepositoryRulesetConditionsType


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems"""

    condition: NotRequired[RepositoryRulesetConditionsType]
    changes: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesType
    ]


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    es
    """

    condition_type: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropConditionTypeType
    ]
    target: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropTargetType
    ]
    include: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropIncludeType
    ]
    exclude: NotRequired[
        WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropExcludeType
    ]


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropConditionTypeType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropConditionType
    """

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropTargetType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropTarget
    """

    from_: NotRequired[str]


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropIncludeType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropInclude
    """

    from_: NotRequired[list[str]]


class WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropExcludeType(
    TypedDict
):
    """WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChang
    esPropExclude
    """

    from_: NotRequired[list[str]]


__all__ = (
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropConditionTypeType",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropExcludeType",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropIncludeType",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesPropTargetType",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsPropChangesType",
    "WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItemsType",
)
