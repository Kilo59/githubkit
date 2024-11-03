"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

import hmac
import json
import importlib
from typing_extensions import TypeAlias
from typing import TYPE_CHECKING, Any, Union, Literal, overload

from githubkit.exception import WebhookTypeNotFound
from githubkit.compat import (
    GitHubModel,
    model_dump,
    type_validate_json,
    type_validate_python,
)

if TYPE_CHECKING:
    from .fork import ForkEvent
    from .meta import MetaEvent
    from .ping import PingEvent
    from .push import PushEvent
    from .star import StarEvent
    from .team import TeamEvent
    from .label import LabelEvent
    from .watch import WatchEvent
    from .create import CreateEvent
    from .delete import DeleteEvent
    from .gollum import GollumEvent
    from .issues import IssuesEvent
    from .member import MemberEvent
    from .public import PublicEvent
    from .status import StatusEvent
    from ._types import WebhookEvent
    from .package import PackageEvent
    from .project import ProjectEvent
    from .release import ReleaseEvent
    from .team_add import TeamAddEvent
    from .check_run import CheckRunEvent
    from .org_block import OrgBlockEvent
    from .milestone import MilestoneEvent
    from .deploy_key import DeployKeyEvent
    from .page_build import PageBuildEvent
    from .sub_issues import SubIssuesEvent
    from .deployment import DeploymentEvent
    from .discussion import DiscussionEvent
    from .membership import MembershipEvent
    from .repository import RepositoryEvent
    from .check_suite import CheckSuiteEvent
    from .merge_group import MergeGroupEvent
    from .projects_v2 import ProjectsV2Event
    from .sponsorship import SponsorshipEvent
    from .project_card import ProjectCardEvent
    from .pull_request import PullRequestEvent
    from .workflow_job import WorkflowJobEvent
    from .workflow_run import WorkflowRunEvent
    from .installation import InstallationEvent
    from .organization import OrganizationEvent
    from .issue_comment import IssueCommentEvent
    from .commit_comment import CommitCommentEvent
    from .project_column import ProjectColumnEvent
    from .custom_property import CustomPropertyEvent
    from .projects_v2_item import ProjectsV2ItemEvent
    from .dependabot_alert import DependabotAlertEvent
    from .registry_package import RegistryPackageEvent
    from .deployment_review import DeploymentReviewEvent
    from .deployment_status import DeploymentStatusEvent
    from .repository_import import RepositoryImportEvent
    from .security_advisory import SecurityAdvisoryEvent
    from .workflow_dispatch import WorkflowDispatchEvent
    from .discussion_comment import DiscussionCommentEvent
    from .repository_ruleset import RepositoryRulesetEvent
    from .code_scanning_alert import CodeScanningAlertEvent
    from .pull_request_review import PullRequestReviewEvent
    from .installation_target import InstallationTargetEvent
    from .repository_advisory import RepositoryAdvisoryEvent
    from .repository_dispatch import RepositoryDispatchEvent
    from .marketplace_purchase import MarketplacePurchaseEvent
    from .secret_scanning_alert import SecretScanningAlertEvent
    from .security_and_analysis import SecurityAndAnalysisEvent
    from .branch_protection_rule import BranchProtectionRuleEvent
    from .custom_property_values import CustomPropertyValuesEvent
    from .github_app_authorization import GithubAppAuthorizationEvent
    from .projects_v2_status_update import ProjectsV2StatusUpdateEvent
    from .installation_repositories import InstallationRepositoriesEvent
    from .pull_request_review_thread import PullRequestReviewThreadEvent
    from .deployment_protection_rule import DeploymentProtectionRuleEvent
    from .pull_request_review_comment import PullRequestReviewCommentEvent
    from .personal_access_token_request import PersonalAccessTokenRequestEvent
    from .exemption_request_push_ruleset import ExemptionRequestPushRulesetEvent
    from .secret_scanning_alert_location import SecretScanningAlertLocationEvent
    from .repository_vulnerability_alert import RepositoryVulnerabilityAlertEvent
    from .branch_protection_configuration import BranchProtectionConfigurationEvent
    from .exemption_request_secret_scanning import ExemptionRequestSecretScanningEvent


EventNameType: TypeAlias = Literal[
    "branch_protection_configuration",
    "branch_protection_rule",
    "exemption_request_push_ruleset",
    "exemption_request_secret_scanning",
    "check_run",
    "check_suite",
    "code_scanning_alert",
    "commit_comment",
    "create",
    "custom_property",
    "custom_property_values",
    "delete",
    "dependabot_alert",
    "deploy_key",
    "deployment",
    "deployment_protection_rule",
    "deployment_review",
    "deployment_status",
    "discussion",
    "discussion_comment",
    "fork",
    "github_app_authorization",
    "gollum",
    "installation",
    "installation_repositories",
    "installation_target",
    "issue_comment",
    "issues",
    "label",
    "marketplace_purchase",
    "member",
    "membership",
    "merge_group",
    "meta",
    "milestone",
    "org_block",
    "organization",
    "package",
    "page_build",
    "personal_access_token_request",
    "ping",
    "project_card",
    "project",
    "project_column",
    "projects_v2",
    "projects_v2_item",
    "projects_v2_status_update",
    "public",
    "pull_request",
    "pull_request_review_comment",
    "pull_request_review",
    "pull_request_review_thread",
    "push",
    "registry_package",
    "release",
    "repository_advisory",
    "repository",
    "repository_dispatch",
    "repository_import",
    "repository_ruleset",
    "repository_vulnerability_alert",
    "secret_scanning_alert",
    "secret_scanning_alert_location",
    "security_advisory",
    "security_and_analysis",
    "sponsorship",
    "star",
    "status",
    "sub_issues",
    "team_add",
    "team",
    "watch",
    "workflow_dispatch",
    "workflow_job",
    "workflow_run",
]
VALID_EVENT_NAMES: set[EventNameType] = {
    "branch_protection_configuration",
    "branch_protection_rule",
    "exemption_request_push_ruleset",
    "exemption_request_secret_scanning",
    "check_run",
    "check_suite",
    "code_scanning_alert",
    "commit_comment",
    "create",
    "custom_property",
    "custom_property_values",
    "delete",
    "dependabot_alert",
    "deploy_key",
    "deployment",
    "deployment_protection_rule",
    "deployment_review",
    "deployment_status",
    "discussion",
    "discussion_comment",
    "fork",
    "github_app_authorization",
    "gollum",
    "installation",
    "installation_repositories",
    "installation_target",
    "issue_comment",
    "issues",
    "label",
    "marketplace_purchase",
    "member",
    "membership",
    "merge_group",
    "meta",
    "milestone",
    "org_block",
    "organization",
    "package",
    "page_build",
    "personal_access_token_request",
    "ping",
    "project_card",
    "project",
    "project_column",
    "projects_v2",
    "projects_v2_item",
    "projects_v2_status_update",
    "public",
    "pull_request",
    "pull_request_review_comment",
    "pull_request_review",
    "pull_request_review_thread",
    "push",
    "registry_package",
    "release",
    "repository_advisory",
    "repository",
    "repository_dispatch",
    "repository_import",
    "repository_ruleset",
    "repository_vulnerability_alert",
    "secret_scanning_alert",
    "secret_scanning_alert_location",
    "security_advisory",
    "security_and_analysis",
    "sponsorship",
    "star",
    "status",
    "sub_issues",
    "team_add",
    "team",
    "watch",
    "workflow_dispatch",
    "workflow_job",
    "workflow_run",
}


class WebhookNamespace:
    @staticmethod
    def parse_without_name(payload: Union[str, bytes]) -> "WebhookEvent":
        """Parse the webhook payload without event name.

        Note:
            Parse the payload without event name is not recommended.

            The parser may take more time to parse the payload and
            the result may not be the correct type as expected.

        Args:
            payload (Union[str, bytes]): webhook payload.
        """
        from ._types import WebhookEvent

        return type_validate_json(WebhookEvent, payload)

    @overload
    @staticmethod
    def parse(
        name: Literal["branch_protection_configuration"], payload: Union[str, bytes]
    ) -> "BranchProtectionConfigurationEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["branch_protection_rule"], payload: Union[str, bytes]
    ) -> "BranchProtectionRuleEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["exemption_request_push_ruleset"], payload: Union[str, bytes]
    ) -> "ExemptionRequestPushRulesetEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["exemption_request_secret_scanning"], payload: Union[str, bytes]
    ) -> "ExemptionRequestSecretScanningEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["check_run"], payload: Union[str, bytes]
    ) -> "CheckRunEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["check_suite"], payload: Union[str, bytes]
    ) -> "CheckSuiteEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["code_scanning_alert"], payload: Union[str, bytes]
    ) -> "CodeScanningAlertEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["commit_comment"], payload: Union[str, bytes]
    ) -> "CommitCommentEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["create"], payload: Union[str, bytes]) -> "CreateEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["custom_property"], payload: Union[str, bytes]
    ) -> "CustomPropertyEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["custom_property_values"], payload: Union[str, bytes]
    ) -> "CustomPropertyValuesEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["delete"], payload: Union[str, bytes]) -> "DeleteEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["dependabot_alert"], payload: Union[str, bytes]
    ) -> "DependabotAlertEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["deploy_key"], payload: Union[str, bytes]
    ) -> "DeployKeyEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["deployment"], payload: Union[str, bytes]
    ) -> "DeploymentEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["deployment_protection_rule"], payload: Union[str, bytes]
    ) -> "DeploymentProtectionRuleEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["deployment_review"], payload: Union[str, bytes]
    ) -> "DeploymentReviewEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["deployment_status"], payload: Union[str, bytes]
    ) -> "DeploymentStatusEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["discussion"], payload: Union[str, bytes]
    ) -> "DiscussionEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["discussion_comment"], payload: Union[str, bytes]
    ) -> "DiscussionCommentEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["fork"], payload: Union[str, bytes]) -> "ForkEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["github_app_authorization"], payload: Union[str, bytes]
    ) -> "GithubAppAuthorizationEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["gollum"], payload: Union[str, bytes]) -> "GollumEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["installation"], payload: Union[str, bytes]
    ) -> "InstallationEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["installation_repositories"], payload: Union[str, bytes]
    ) -> "InstallationRepositoriesEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["installation_target"], payload: Union[str, bytes]
    ) -> "InstallationTargetEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["issue_comment"], payload: Union[str, bytes]
    ) -> "IssueCommentEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["issues"], payload: Union[str, bytes]) -> "IssuesEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["label"], payload: Union[str, bytes]) -> "LabelEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["marketplace_purchase"], payload: Union[str, bytes]
    ) -> "MarketplacePurchaseEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["member"], payload: Union[str, bytes]) -> "MemberEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["membership"], payload: Union[str, bytes]
    ) -> "MembershipEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["merge_group"], payload: Union[str, bytes]
    ) -> "MergeGroupEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["meta"], payload: Union[str, bytes]) -> "MetaEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["milestone"], payload: Union[str, bytes]
    ) -> "MilestoneEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["org_block"], payload: Union[str, bytes]
    ) -> "OrgBlockEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["organization"], payload: Union[str, bytes]
    ) -> "OrganizationEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["package"], payload: Union[str, bytes]
    ) -> "PackageEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["page_build"], payload: Union[str, bytes]
    ) -> "PageBuildEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["personal_access_token_request"], payload: Union[str, bytes]
    ) -> "PersonalAccessTokenRequestEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["ping"], payload: Union[str, bytes]) -> "PingEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["project_card"], payload: Union[str, bytes]
    ) -> "ProjectCardEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["project"], payload: Union[str, bytes]
    ) -> "ProjectEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["project_column"], payload: Union[str, bytes]
    ) -> "ProjectColumnEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["projects_v2"], payload: Union[str, bytes]
    ) -> "ProjectsV2Event": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["projects_v2_item"], payload: Union[str, bytes]
    ) -> "ProjectsV2ItemEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["projects_v2_status_update"], payload: Union[str, bytes]
    ) -> "ProjectsV2StatusUpdateEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["public"], payload: Union[str, bytes]) -> "PublicEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["pull_request"], payload: Union[str, bytes]
    ) -> "PullRequestEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["pull_request_review_comment"], payload: Union[str, bytes]
    ) -> "PullRequestReviewCommentEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["pull_request_review"], payload: Union[str, bytes]
    ) -> "PullRequestReviewEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["pull_request_review_thread"], payload: Union[str, bytes]
    ) -> "PullRequestReviewThreadEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["push"], payload: Union[str, bytes]) -> "PushEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["registry_package"], payload: Union[str, bytes]
    ) -> "RegistryPackageEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["release"], payload: Union[str, bytes]
    ) -> "ReleaseEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["repository_advisory"], payload: Union[str, bytes]
    ) -> "RepositoryAdvisoryEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["repository"], payload: Union[str, bytes]
    ) -> "RepositoryEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["repository_dispatch"], payload: Union[str, bytes]
    ) -> "RepositoryDispatchEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["repository_import"], payload: Union[str, bytes]
    ) -> "RepositoryImportEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["repository_ruleset"], payload: Union[str, bytes]
    ) -> "RepositoryRulesetEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["repository_vulnerability_alert"], payload: Union[str, bytes]
    ) -> "RepositoryVulnerabilityAlertEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["secret_scanning_alert"], payload: Union[str, bytes]
    ) -> "SecretScanningAlertEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["secret_scanning_alert_location"], payload: Union[str, bytes]
    ) -> "SecretScanningAlertLocationEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["security_advisory"], payload: Union[str, bytes]
    ) -> "SecurityAdvisoryEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["security_and_analysis"], payload: Union[str, bytes]
    ) -> "SecurityAndAnalysisEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["sponsorship"], payload: Union[str, bytes]
    ) -> "SponsorshipEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["star"], payload: Union[str, bytes]) -> "StarEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["status"], payload: Union[str, bytes]) -> "StatusEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["sub_issues"], payload: Union[str, bytes]
    ) -> "SubIssuesEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["team_add"], payload: Union[str, bytes]
    ) -> "TeamAddEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["team"], payload: Union[str, bytes]) -> "TeamEvent": ...
    @overload
    @staticmethod
    def parse(name: Literal["watch"], payload: Union[str, bytes]) -> "WatchEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["workflow_dispatch"], payload: Union[str, bytes]
    ) -> "WorkflowDispatchEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["workflow_job"], payload: Union[str, bytes]
    ) -> "WorkflowJobEvent": ...
    @overload
    @staticmethod
    def parse(
        name: Literal["workflow_run"], payload: Union[str, bytes]
    ) -> "WorkflowRunEvent": ...

    @overload
    @staticmethod
    def parse(name: EventNameType, payload: Union[str, bytes]) -> "WebhookEvent": ...

    @overload
    @staticmethod
    def parse(name: str, payload: Union[str, bytes]) -> "WebhookEvent": ...

    @staticmethod
    def parse(
        name: Union[EventNameType, str], payload: Union[str, bytes]
    ) -> "WebhookEvent":
        """Parse the webhook payload with event name.

        Args:
            name (EventNameType): event name.
            payload (Union[str, bytes]): webhook payload.
        """
        if name not in VALID_EVENT_NAMES:
            raise WebhookTypeNotFound(name)
        module = importlib.import_module(f".{name}", __package__)
        Event = getattr(module, "Event")
        return type_validate_json(Event, payload)

    @staticmethod
    def parse_obj_without_name(payload: dict[str, Any]) -> "WebhookEvent":
        """Parse the webhook payload dict without event name.

        Note:
            Parse the payload without event name is not recommended.

            The parser may take more time to parse the payload and
            the result may not be the correct type as expected.

        Args:
            payload (dict[str, Any]): webhook payload dict.
        """

        from ._types import WebhookEvent

        return type_validate_python(WebhookEvent, payload)

    @overload
    @staticmethod
    def parse_obj(
        name: Literal["branch_protection_configuration"], payload: dict[str, Any]
    ) -> "BranchProtectionConfigurationEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["branch_protection_rule"], payload: dict[str, Any]
    ) -> "BranchProtectionRuleEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["exemption_request_push_ruleset"], payload: dict[str, Any]
    ) -> "ExemptionRequestPushRulesetEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["exemption_request_secret_scanning"], payload: dict[str, Any]
    ) -> "ExemptionRequestSecretScanningEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["check_run"], payload: dict[str, Any]
    ) -> "CheckRunEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["check_suite"], payload: dict[str, Any]
    ) -> "CheckSuiteEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["code_scanning_alert"], payload: dict[str, Any]
    ) -> "CodeScanningAlertEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["commit_comment"], payload: dict[str, Any]
    ) -> "CommitCommentEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["create"], payload: dict[str, Any]
    ) -> "CreateEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["custom_property"], payload: dict[str, Any]
    ) -> "CustomPropertyEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["custom_property_values"], payload: dict[str, Any]
    ) -> "CustomPropertyValuesEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["delete"], payload: dict[str, Any]
    ) -> "DeleteEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["dependabot_alert"], payload: dict[str, Any]
    ) -> "DependabotAlertEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["deploy_key"], payload: dict[str, Any]
    ) -> "DeployKeyEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["deployment"], payload: dict[str, Any]
    ) -> "DeploymentEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["deployment_protection_rule"], payload: dict[str, Any]
    ) -> "DeploymentProtectionRuleEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["deployment_review"], payload: dict[str, Any]
    ) -> "DeploymentReviewEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["deployment_status"], payload: dict[str, Any]
    ) -> "DeploymentStatusEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["discussion"], payload: dict[str, Any]
    ) -> "DiscussionEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["discussion_comment"], payload: dict[str, Any]
    ) -> "DiscussionCommentEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["fork"], payload: dict[str, Any]) -> "ForkEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["github_app_authorization"], payload: dict[str, Any]
    ) -> "GithubAppAuthorizationEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["gollum"], payload: dict[str, Any]
    ) -> "GollumEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["installation"], payload: dict[str, Any]
    ) -> "InstallationEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["installation_repositories"], payload: dict[str, Any]
    ) -> "InstallationRepositoriesEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["installation_target"], payload: dict[str, Any]
    ) -> "InstallationTargetEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["issue_comment"], payload: dict[str, Any]
    ) -> "IssueCommentEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["issues"], payload: dict[str, Any]
    ) -> "IssuesEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["label"], payload: dict[str, Any]) -> "LabelEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["marketplace_purchase"], payload: dict[str, Any]
    ) -> "MarketplacePurchaseEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["member"], payload: dict[str, Any]
    ) -> "MemberEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["membership"], payload: dict[str, Any]
    ) -> "MembershipEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["merge_group"], payload: dict[str, Any]
    ) -> "MergeGroupEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["meta"], payload: dict[str, Any]) -> "MetaEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["milestone"], payload: dict[str, Any]
    ) -> "MilestoneEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["org_block"], payload: dict[str, Any]
    ) -> "OrgBlockEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["organization"], payload: dict[str, Any]
    ) -> "OrganizationEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["package"], payload: dict[str, Any]
    ) -> "PackageEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["page_build"], payload: dict[str, Any]
    ) -> "PageBuildEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["personal_access_token_request"], payload: dict[str, Any]
    ) -> "PersonalAccessTokenRequestEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["ping"], payload: dict[str, Any]) -> "PingEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["project_card"], payload: dict[str, Any]
    ) -> "ProjectCardEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["project"], payload: dict[str, Any]
    ) -> "ProjectEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["project_column"], payload: dict[str, Any]
    ) -> "ProjectColumnEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["projects_v2"], payload: dict[str, Any]
    ) -> "ProjectsV2Event": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["projects_v2_item"], payload: dict[str, Any]
    ) -> "ProjectsV2ItemEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["projects_v2_status_update"], payload: dict[str, Any]
    ) -> "ProjectsV2StatusUpdateEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["public"], payload: dict[str, Any]
    ) -> "PublicEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["pull_request"], payload: dict[str, Any]
    ) -> "PullRequestEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["pull_request_review_comment"], payload: dict[str, Any]
    ) -> "PullRequestReviewCommentEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["pull_request_review"], payload: dict[str, Any]
    ) -> "PullRequestReviewEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["pull_request_review_thread"], payload: dict[str, Any]
    ) -> "PullRequestReviewThreadEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["push"], payload: dict[str, Any]) -> "PushEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["registry_package"], payload: dict[str, Any]
    ) -> "RegistryPackageEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["release"], payload: dict[str, Any]
    ) -> "ReleaseEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["repository_advisory"], payload: dict[str, Any]
    ) -> "RepositoryAdvisoryEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["repository"], payload: dict[str, Any]
    ) -> "RepositoryEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["repository_dispatch"], payload: dict[str, Any]
    ) -> "RepositoryDispatchEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["repository_import"], payload: dict[str, Any]
    ) -> "RepositoryImportEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["repository_ruleset"], payload: dict[str, Any]
    ) -> "RepositoryRulesetEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["repository_vulnerability_alert"], payload: dict[str, Any]
    ) -> "RepositoryVulnerabilityAlertEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["secret_scanning_alert"], payload: dict[str, Any]
    ) -> "SecretScanningAlertEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["secret_scanning_alert_location"], payload: dict[str, Any]
    ) -> "SecretScanningAlertLocationEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["security_advisory"], payload: dict[str, Any]
    ) -> "SecurityAdvisoryEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["security_and_analysis"], payload: dict[str, Any]
    ) -> "SecurityAndAnalysisEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["sponsorship"], payload: dict[str, Any]
    ) -> "SponsorshipEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["star"], payload: dict[str, Any]) -> "StarEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["status"], payload: dict[str, Any]
    ) -> "StatusEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["sub_issues"], payload: dict[str, Any]
    ) -> "SubIssuesEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["team_add"], payload: dict[str, Any]
    ) -> "TeamAddEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["team"], payload: dict[str, Any]) -> "TeamEvent": ...
    @overload
    @staticmethod
    def parse_obj(name: Literal["watch"], payload: dict[str, Any]) -> "WatchEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["workflow_dispatch"], payload: dict[str, Any]
    ) -> "WorkflowDispatchEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["workflow_job"], payload: dict[str, Any]
    ) -> "WorkflowJobEvent": ...
    @overload
    @staticmethod
    def parse_obj(
        name: Literal["workflow_run"], payload: dict[str, Any]
    ) -> "WorkflowRunEvent": ...

    @overload
    @staticmethod
    def parse_obj(name: EventNameType, payload: dict[str, Any]) -> "WebhookEvent": ...

    @overload
    @staticmethod
    def parse_obj(name: str, payload: dict[str, Any]) -> "WebhookEvent": ...

    @staticmethod
    def parse_obj(
        name: Union[EventNameType, str], payload: dict[str, Any]
    ) -> "WebhookEvent":
        """Parse the webhook payload dict with event name.

        Args:
            name (EventNameType): event name.
            payload (dict[str, Any]): webhook payload dict.
        """

        if name not in VALID_EVENT_NAMES:
            raise WebhookTypeNotFound(name)
        module = importlib.import_module(f".{name}", __package__)
        Event = getattr(module, "Event")
        return type_validate_python(Event, payload)

    @staticmethod
    def normalize_payload(payload: Union[GitHubModel, dict[str, Any]]) -> str:
        """Normalize the webhook payload to string.

        Note:
            This function may not behave the same way as GitHub Webhooks.

            Always use raw data posted by GitHub Webhooks.

        Args:
            payload (Union[GitHubModel, dict[str, Any]]): webhook payload.

        Returns:
            str: normalized payload string.
        """
        payload = model_dump(payload) if isinstance(payload, GitHubModel) else payload
        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

    @staticmethod
    def sign(
        secret: str,
        payload: Union[GitHubModel, dict[str, Any], str, bytes],
        method: Literal["sha256", "sha1"] = "sha256",
    ) -> str:
        """Sign the webhook payload.

        Args:
            secret (str): webhook secret.
            payload (Union[GitHubModel, dict[str, Any], str, bytes]): webhook payload.
            method (str): sha256 or sha1. Defaults to sha256.

        Returns:
            str: signed payload string.
        """
        norm_payload = (
            payload
            if isinstance(payload, (str, bytes))
            else WebhookNamespace.normalize_payload(payload)
        )
        hmac_hex = hmac.new(
            secret.encode("utf-8"),
            norm_payload.encode("utf-8")
            if isinstance(norm_payload, str)
            else norm_payload,
            method,
        ).hexdigest()
        return f"{method}={hmac_hex}"

    @staticmethod
    def verify(
        secret: str,
        payload: Union[GitHubModel, dict[str, Any], str, bytes],
        signature: str,
    ) -> bool:
        """Verify the webhook payload.

        See: https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks#validating-payloads-from-github

        Note:
            Always use raw data posted by GitHub Webhooks.

        Args:
            secret (str): webhook secret.
            payload (Union[GitHubModel, dict[str, Any], str, bytes]): webhook payload.
            signature (str): webhook signature.

        Returns:
            bool: True if verified, False otherwise.
        """
        signed = WebhookNamespace.sign(
            secret, payload, "sha256" if signature.startswith("sha256=") else "sha1"
        )

        # use time safe comparison
        return hmac.compare_digest(signed, signature)
