"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild
from githubkit.typing import Missing
from githubkit.utils import UNSET

from .group_0002 import SimpleUser
from .group_0389 import EnterpriseWebhooks
from .group_0390 import SimpleInstallation
from .group_0391 import OrganizationSimpleWebhooks
from .group_0392 import RepositoryWebhooks


class WebhookCodeScanningAlertCreated(GitHubModel):
    """code_scanning_alert created event"""

    action: Literal["created"] = Field()
    alert: WebhookCodeScanningAlertCreatedPropAlert = Field(
        description="The code scanning alert involved in the event."
    )
    commit_oid: str = Field(
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    ref: str = Field(
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUser = Field(title="Simple User", description="A GitHub user.")


class WebhookCodeScanningAlertCreatedPropAlert(GitHubModel):
    """WebhookCodeScanningAlertCreatedPropAlert

    The code scanning alert involved in the event.
    """

    created_at: Union[datetime, None] = Field(
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`"
    )
    dismissed_at: None = Field(
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_by: None = Field()
    dismissed_comment: Missing[Union[Annotated[str, Field(max_length=280)], None]] = (
        Field(
            default=UNSET,
            description="The dismissal comment associated with the dismissal of the alert.",
        )
    )
    dismissed_reason: None = Field(
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`."
    )
    fixed_at: Missing[None] = Field(default=UNSET)
    html_url: str = Field(description="The GitHub URL of the alert resource.")
    instances_url: Missing[str] = Field(default=UNSET)
    most_recent_instance: Missing[
        Union[WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstance, None]
    ] = Field(default=UNSET, title="Alert Instance")
    number: int = Field(description="The code scanning alert number.")
    rule: WebhookCodeScanningAlertCreatedPropAlertPropRule = Field()
    state: Union[None, Literal["open", "dismissed"]] = Field(
        description="State of a code scanning alert."
    )
    tool: Union[WebhookCodeScanningAlertCreatedPropAlertPropTool, None] = Field()
    updated_at: Missing[Union[str, None]] = Field(default=UNSET)
    url: str = Field()


class WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstance(GitHubModel):
    """Alert Instance"""

    analysis_key: str = Field(
        description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name."
    )
    category: Missing[str] = Field(
        default=UNSET,
        description="Identifies the configuration under which the analysis was executed.",
    )
    classifications: Missing[list[str]] = Field(default=UNSET)
    commit_sha: Missing[str] = Field(default=UNSET)
    environment: str = Field(
        description="Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed."
    )
    location: Missing[
        WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocation
    ] = Field(default=UNSET)
    message: Missing[
        WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessage
    ] = Field(default=UNSET)
    ref: str = Field(
        description="The full Git reference, formatted as `refs/heads/<branch name>`."
    )
    state: Literal["open", "dismissed", "fixed"] = Field(
        description="State of a code scanning alert."
    )


class WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocation(
    GitHubModel
):
    """WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocation"""

    end_column: Missing[int] = Field(default=UNSET)
    end_line: Missing[int] = Field(default=UNSET)
    path: Missing[str] = Field(default=UNSET)
    start_column: Missing[int] = Field(default=UNSET)
    start_line: Missing[int] = Field(default=UNSET)


class WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessage(
    GitHubModel
):
    """WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessage"""

    text: Missing[str] = Field(default=UNSET)


class WebhookCodeScanningAlertCreatedPropAlertPropRule(GitHubModel):
    """WebhookCodeScanningAlertCreatedPropAlertPropRule"""

    description: str = Field(
        description="A short description of the rule used to detect the alert."
    )
    full_description: Missing[str] = Field(default=UNSET)
    help_: Missing[Union[str, None]] = Field(default=UNSET, alias="help")
    help_uri: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="A link to the documentation for the rule used to detect the alert.",
    )
    id: str = Field(
        description="A unique identifier for the rule used to detect the alert."
    )
    name: Missing[str] = Field(default=UNSET)
    severity: Union[None, Literal["none", "note", "warning", "error"]] = Field(
        description="The severity of the alert."
    )
    tags: Missing[Union[list[str], None]] = Field(default=UNSET)


class WebhookCodeScanningAlertCreatedPropAlertPropTool(GitHubModel):
    """WebhookCodeScanningAlertCreatedPropAlertPropTool"""

    guid: Missing[Union[str, None]] = Field(default=UNSET)
    name: str = Field(
        description="The name of the tool used to generate the code scanning analysis alert."
    )
    version: Union[str, None] = Field(
        description="The version of the tool used to detect the alert."
    )


model_rebuild(WebhookCodeScanningAlertCreated)
model_rebuild(WebhookCodeScanningAlertCreatedPropAlert)
model_rebuild(WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstance)
model_rebuild(
    WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocation
)
model_rebuild(WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessage)
model_rebuild(WebhookCodeScanningAlertCreatedPropAlertPropRule)
model_rebuild(WebhookCodeScanningAlertCreatedPropAlertPropTool)

__all__ = (
    "WebhookCodeScanningAlertCreated",
    "WebhookCodeScanningAlertCreatedPropAlert",
    "WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstance",
    "WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropLocation",
    "WebhookCodeScanningAlertCreatedPropAlertPropMostRecentInstancePropMessage",
    "WebhookCodeScanningAlertCreatedPropAlertPropRule",
    "WebhookCodeScanningAlertCreatedPropAlertPropTool",
)
