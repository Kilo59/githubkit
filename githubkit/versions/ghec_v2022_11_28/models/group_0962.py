"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ProjectsColumnsCardsCardIdMovesPostBody(GitHubModel):
    """ProjectsColumnsCardsCardIdMovesPostBody"""

    position: str = Field(
        pattern="^(?:top|bottom|after:\\d+)$",
        description="The position of the card in a column. Can be one of: `top`, `bottom`, or `after:<card_id>` to place after the specified card.",
    )
    column_id: Missing[int] = Field(
        default=UNSET,
        description="The unique identifier of the column the card should be moved to",
    )


model_rebuild(ProjectsColumnsCardsCardIdMovesPostBody)

__all__ = ("ProjectsColumnsCardsCardIdMovesPostBody",)
