from functools import partial

import pytest

from githubkit import GitHub
from githubkit.versions import LATEST_VERSION
from githubkit.versions.latest.models import FullRepository

OWNER = "yanyongyu"
REPO = "githubkit"


def test_call(g: GitHub):
    resp = g.rest.repos.get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)


@pytest.mark.anyio
async def test_async_call(g: GitHub):
    resp = await g.rest.repos.async_get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)


def test_versioned_call(g: GitHub):
    resp = g.rest(LATEST_VERSION).repos.get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)


@pytest.mark.anyio
async def test_versioned_async_call(g: GitHub):
    resp = await g.rest(LATEST_VERSION).repos.async_get(OWNER, REPO)
    assert isinstance(resp.parsed_data, FullRepository)


def test_call_with_body(g: GitHub):
    resp = g.rest.markdown.render(text="Hello **world**")
    assert isinstance(resp.text, str)


@pytest.mark.anyio
async def test_async_call_with_body(g: GitHub):
    resp = await g.rest.markdown.async_render(text="Hello **world**")
    assert isinstance(resp.text, str)


def test_call_with_raw_body(g: GitHub):
    resp = g.rest.markdown.render_raw(data="Hello **world**")
    assert isinstance(resp.text, str)


@pytest.mark.anyio
async def test_async_call_with_raw_body(g: GitHub):
    resp = await g.rest.markdown.async_render_raw(data="Hello **world**")
    assert isinstance(resp.text, str)


def test_paginate(g: GitHub):
    paginator = g.rest.paginate(
        g.rest.issues.list_for_repo, owner=OWNER, repo=REPO, per_page=50
    )
    for _ in paginator:
        ...


def test_paginate_with_partial(g: GitHub):
    paginator = g.rest.paginate(
        partial(g.rest.issues.list_for_repo, OWNER, REPO), per_page=50
    )
    for _ in paginator:
        ...


@pytest.mark.anyio
async def test_async_paginate(g: GitHub):
    paginator = g.rest.paginate(
        g.rest.issues.async_list_for_repo, owner=OWNER, repo=REPO, per_page=50
    )
    async for _ in paginator:
        ...


@pytest.mark.anyio
async def test_async_paginate_with_partial(g: GitHub):
    paginator = g.rest.paginate(
        partial(g.rest.issues.async_list_for_repo, OWNER, REPO),
        per_page=50,
    )
    async for _ in paginator:
        ...
