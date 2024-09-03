"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import Annotated

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class CustomProperty(GitHubModel):
    """Organization Custom Property

    Custom property defined on an organization
    """

    property_name: str = Field(description="The name of the property")
    url: Missing[str] = Field(
        default=UNSET,
        description="The URL that can be used to fetch, update, or delete info about this property via the API.",
    )
    value_type: Literal["string", "single_select", "multi_select", "true_false"] = (
        Field(description="The type of the value for the property")
    )
    required: Missing[bool] = Field(
        default=UNSET, description="Whether the property is required."
    )
    default_value: Missing[Union[str, List[str], None]] = Field(
        default=UNSET, description="Default value of the property"
    )
    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="Short description of the property"
    )
    allowed_values: Missing[
        Union[
            Annotated[
                List[Annotated[str, Field(max_length=75)]], Field(max_length=200)
            ],
            None,
        ]
    ] = Field(
        default=UNSET,
        description="An ordered list of the allowed values of the property.\nThe property can have up to 200 allowed values.",
    )
    values_editable_by: Missing[
        Union[None, Literal["org_actors", "org_and_repo_actors"]]
    ] = Field(default=UNSET, description="Who can edit the values of the property")


model_rebuild(CustomProperty)

__all__ = ("CustomProperty",)
