import uuid

from django.test import RequestFactory
from django.test import SimpleTestCase
from django.test.utils import override_settings

from django_cloudflare import CloudflareMiddleware
from django_cloudflare.constants import DjangoCloudflareDefaultAttr
from django_cloudflare.constants import DjangoCloudflareHeader


class CloudflareMiddlewareTests(SimpleTestCase):
    request_factory = RequestFactory()
    headers = {
        DjangoCloudflareHeader.cdn_loop: "cloudflare",
        DjangoCloudflareHeader.ip: "127.0.0.1",
        DjangoCloudflareHeader.country: "PL",
        DjangoCloudflareHeader.ray: "123456789-WAW",
        DjangoCloudflareHeader.warp_tag: str(uuid.uuid4()),
    }
    django_headers = {
        f"HTTP_{key}".upper(): value for key, value in headers.items()
    }

    def setUp(self):
        self.middleware = CloudflareMiddleware(lambda x: x)

    @override_settings(
        CF_HEADER_CDN_LOOP_ENABLED=True,
        CF_HEADER_IP_ENABLED=True,
        CF_HEADER_COUNTRY_ENABLED=True,
        CF_HEADER_RAY_ENABLED=True,
        CF_HEADER_WARP_TAG_ENABLED=True,
    )
    def test_headers_enabled(self):
        request = self.request_factory.get("/", **self.django_headers)
        self.middleware(request)
        for header_key, attr_name in zip(
            DjangoCloudflareHeader, DjangoCloudflareDefaultAttr
        ):
            self.assertEqual(
                getattr(request, attr_name), self.headers[header_key]
            )

    @override_settings(
        CF_HEADER_CDN_LOOP_ENABLED=True,
        CF_HEADER_IP_ENABLED=True,
        CF_HEADER_COUNTRY_ENABLED=True,
        CF_HEADER_RAY_ENABLED=True,
        CF_HEADER_WARP_TAG_ENABLED=True,
    )
    def test_headers_enabled_not_present_in_request_headers(self):
        request = self.request_factory.get("/")
        self.middleware(request)
        for header_key, attr_name in zip(
            DjangoCloudflareHeader, DjangoCloudflareDefaultAttr
        ):
            self.assertTrue(hasattr(request, attr_name))
            self.assertEqual(getattr(request, attr_name), None)

    @override_settings(
        CF_HEADER_CDN_LOOP_ENABLED=False,
        CF_HEADER_IP_ENABLED=False,
        CF_HEADER_COUNTRY_ENABLED=False,
        CF_HEADER_RAY_ENABLED=False,
        CF_HEADER_WARP_TAG_ENABLED=False,
    )
    def test_headers_disabled(self):
        request = self.request_factory.get("/", **self.django_headers)
        self.middleware(request)
        for header_key, attr_name in zip(
            DjangoCloudflareHeader, DjangoCloudflareDefaultAttr
        ):
            self.assertIn(header_key, self.headers)
            self.assertFalse(hasattr(request, attr_name))

    @override_settings(CF_HEADER_IP_ENABLED=True, CF_HEADER_IP_ATTR_NAME="ip")
    def test_set_custom_attr_name(self):
        request = self.request_factory.get("/", **self.django_headers)
        self.middleware(request)
        assert (
            getattr(request, "ip") == self.headers[DjangoCloudflareHeader.ip]
        )
