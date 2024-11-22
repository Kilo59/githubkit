"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class PrivateVulnerabilityReportCreate(GitHubModel):
    """PrivateVulnerabilityReportCreate"""

    summary: str = Field(
        max_length=1024, description="A short summary of the advisory."
    )
    description: str = Field(
        max_length=65535,
        description="A detailed description of what the advisory impacts.",
    )
    vulnerabilities: Missing[
        Union[list[PrivateVulnerabilityReportCreatePropVulnerabilitiesItems], None]
    ] = Field(
        default=UNSET,
        description="An array of products affected by the vulnerability detailed in a repository security advisory.",
    )
    cwe_ids: Missing[Union[list[str], None]] = Field(
        default=UNSET, description="A list of Common Weakness Enumeration (CWE) IDs."
    )
    severity: Missing[Union[None, Literal["critical", "high", "medium", "low"]]] = (
        Field(
            default=UNSET,
            description="The severity of the advisory. You must choose between setting this field or `cvss_vector_string`.",
        )
    )
    cvss_vector_string: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The CVSS vector that calculates the severity of the advisory. You must choose between setting this field or `severity`.",
    )
    start_private_fork: Missing[bool] = Field(
        default=UNSET,
        description="Whether to create a temporary private fork of the repository to collaborate on a fix.",
    )


class PrivateVulnerabilityReportCreatePropVulnerabilitiesItems(GitHubModel):
    """PrivateVulnerabilityReportCreatePropVulnerabilitiesItems"""

    package: PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsPropPackage = (
        Field(description="The name of the package affected by the vulnerability.")
    )
    vulnerable_version_range: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The range of the package versions affected by the vulnerability.",
    )
    patched_versions: Missing[Union[str, None]] = Field(
        default=UNSET,
        description="The package version(s) that resolve the vulnerability.",
    )
    vulnerable_functions: Missing[Union[list[str], None]] = Field(
        default=UNSET, description="The functions in the package that are affected."
    )


class PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsPropPackage(GitHubModel):
    """PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsPropPackage

    The name of the package affected by the vulnerability.
    """

    ecosystem: Literal[
        "rubygems",
        "npm",
        "pip",
        "maven",
        "nuget",
        "composer",
        "go",
        "rust",
        "erlang",
        "actions",
        "pub",
        "other",
        "swift",
    ] = Field(description="The package's language or package management ecosystem.")
    name: Missing[Union[str, None]] = Field(
        default=UNSET, description="The unique package name within its ecosystem."
    )


model_rebuild(PrivateVulnerabilityReportCreate)
model_rebuild(PrivateVulnerabilityReportCreatePropVulnerabilitiesItems)
model_rebuild(PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsPropPackage)

__all__ = (
    "PrivateVulnerabilityReportCreate",
    "PrivateVulnerabilityReportCreatePropVulnerabilitiesItems",
    "PrivateVulnerabilityReportCreatePropVulnerabilitiesItemsPropPackage",
)
