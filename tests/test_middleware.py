import uuid

import pytest
from asgiref.sync import iscoroutinefunction
from django.test import RequestFactory, override_settings

from django_cloudflare import CloudflareMiddleware
from django_cloudflare.constants import (
    DjangoCloudflareDefaultAttr,
    DjangoCloudflareHeader,
)

HEADERS = {
    DjangoCloudflareHeader.cdn_loop: "cloudflare",
    DjangoCloudflareHeader.ip: "127.0.0.1",
    DjangoCloudflareHeader.ipv6: "2001:db8::1",
    DjangoCloudflareHeader.country: "PL",
    DjangoCloudflareHeader.ray: "123456789-WAW",
    DjangoCloudflareHeader.visitor: '{"scheme":"https"}',
    DjangoCloudflareHeader.warp_tag: str(uuid.uuid4()),
    DjangoCloudflareHeader.forwarded_for: "203.0.113.1, 198.51.100.1",
    DjangoCloudflareHeader.forwarded_proto: "https",
}
DJANGO_HEADERS = {
    f"HTTP_{key}".upper(): value for key, value in HEADERS.items()
}

ALL_ENABLED = {
    "CF_HEADER_CDN_LOOP_ENABLED": True,
    "CF_HEADER_IP_ENABLED": True,
    "CF_HEADER_IPV6_ENABLED": True,
    "CF_HEADER_COUNTRY_ENABLED": True,
    "CF_HEADER_RAY_ENABLED": True,
    "CF_HEADER_VISITOR_ENABLED": True,
    "CF_HEADER_WARP_TAG_ENABLED": True,
    "CF_HEADER_FORWARDED_FOR_ENABLED": True,
    "CF_HEADER_FORWARDED_PROTO_ENABLED": True,
}

ALL_DISABLED = {
    "CF_HEADER_CDN_LOOP_ENABLED": False,
    "CF_HEADER_IP_ENABLED": False,
    "CF_HEADER_IPV6_ENABLED": False,
    "CF_HEADER_COUNTRY_ENABLED": False,
    "CF_HEADER_RAY_ENABLED": False,
    "CF_HEADER_VISITOR_ENABLED": False,
    "CF_HEADER_WARP_TAG_ENABLED": False,
    "CF_HEADER_FORWARDED_FOR_ENABLED": False,
    "CF_HEADER_FORWARDED_PROTO_ENABLED": False,
}


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def sync_middleware():
    return CloudflareMiddleware(lambda request: request)


@override_settings(**ALL_ENABLED)
def test_headers_enabled(rf, sync_middleware):
    request = rf.get("/", **DJANGO_HEADERS)
    sync_middleware(request)
    for header_key, attr_name in zip(
        DjangoCloudflareHeader, DjangoCloudflareDefaultAttr
    ):
        assert getattr(request, attr_name) == HEADERS[header_key]


@override_settings(**ALL_ENABLED)
def test_headers_enabled_not_present_in_request(rf, sync_middleware):
    request = rf.get("/")
    sync_middleware(request)
    for attr_name in DjangoCloudflareDefaultAttr:
        assert hasattr(request, attr_name)
        assert getattr(request, attr_name) is None


@override_settings(**ALL_DISABLED)
def test_headers_disabled(rf, sync_middleware):
    request = rf.get("/", **DJANGO_HEADERS)
    sync_middleware(request)
    for attr_name in DjangoCloudflareDefaultAttr:
        assert not hasattr(request, attr_name)


@override_settings(CF_HEADER_IP_ENABLED=True, CF_HEADER_IP_ATTR_NAME="ip")
def test_custom_attr_name(rf, sync_middleware):
    request = rf.get("/", **DJANGO_HEADERS)
    sync_middleware(request)
    assert getattr(request, "ip") == HEADERS[DjangoCloudflareHeader.ip]


@override_settings(CF_HEADER_IP_ENABLED=True, CF_HEADER_COUNTRY_ENABLED=True)
def test_selective_headers(rf, sync_middleware):
    request = rf.get("/", **DJANGO_HEADERS)
    sync_middleware(request)
    assert hasattr(request, DjangoCloudflareDefaultAttr.cf_ip)
    assert hasattr(request, DjangoCloudflareDefaultAttr.cf_country)
    assert not hasattr(request, DjangoCloudflareDefaultAttr.cf_cdn_loop)
    assert not hasattr(request, DjangoCloudflareDefaultAttr.cf_ipv6)
    assert not hasattr(request, DjangoCloudflareDefaultAttr.cf_ray)
    assert not hasattr(request, DjangoCloudflareDefaultAttr.cf_visitor)
    assert not hasattr(request, DjangoCloudflareDefaultAttr.cf_warp_tag)
    assert not hasattr(request, DjangoCloudflareDefaultAttr.cf_forwarded_for)
    assert not hasattr(request, DjangoCloudflareDefaultAttr.cf_forwarded_proto)


def test_default_no_settings(rf, sync_middleware):
    """Without any CF_HEADER_*_ENABLED settings, no attrs are set."""
    request = rf.get("/", **DJANGO_HEADERS)
    sync_middleware(request)
    for attr_name in DjangoCloudflareDefaultAttr:
        assert not hasattr(request, attr_name)


@override_settings(**ALL_ENABLED)
def test_empty_header_values(rf, sync_middleware):
    empty_headers = {
        f"HTTP_{key}".upper(): "" for key in DjangoCloudflareHeader
    }
    request = rf.get("/", **empty_headers)
    sync_middleware(request)
    for attr_name in DjangoCloudflareDefaultAttr:
        assert getattr(request, attr_name) == ""


# --- Async tests ---


@pytest.fixture
def async_middleware():
    async def async_response(request):
        return request

    return CloudflareMiddleware(async_response)


def test_async_middleware_is_coroutine(async_middleware):
    assert iscoroutinefunction(async_middleware)


def test_sync_middleware_is_not_coroutine(sync_middleware):
    assert not iscoroutinefunction(sync_middleware)


@pytest.mark.asyncio
@override_settings(**ALL_ENABLED)
async def test_async_headers_enabled(rf, async_middleware):
    request = rf.get("/", **DJANGO_HEADERS)
    await async_middleware(request)
    for header_key, attr_name in zip(
        DjangoCloudflareHeader, DjangoCloudflareDefaultAttr
    ):
        assert getattr(request, attr_name) == HEADERS[header_key]


@pytest.mark.asyncio
@override_settings(**ALL_DISABLED)
async def test_async_headers_disabled(rf, async_middleware):
    request = rf.get("/", **DJANGO_HEADERS)
    await async_middleware(request)
    for attr_name in DjangoCloudflareDefaultAttr:
        assert not hasattr(request, attr_name)


@pytest.mark.asyncio
@override_settings(**ALL_ENABLED)
async def test_async_headers_not_present(rf, async_middleware):
    request = rf.get("/")
    await async_middleware(request)
    for attr_name in DjangoCloudflareDefaultAttr:
        assert hasattr(request, attr_name)
        assert getattr(request, attr_name) is None
