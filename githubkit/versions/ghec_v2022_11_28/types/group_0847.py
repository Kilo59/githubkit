"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict

from .group_0036 import RunnerType


class EnterprisesEnterpriseActionsRunnersGenerateJitconfigPostResponse201Type(
    TypedDict
):
    """EnterprisesEnterpriseActionsRunnersGenerateJitconfigPostResponse201"""

    runner: RunnerType
    encoded_jit_config: str


__all__ = ("EnterprisesEnterpriseActionsRunnersGenerateJitconfigPostResponse201Type",)
