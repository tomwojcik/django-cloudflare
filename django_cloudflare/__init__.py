import dataclasses
import typing

from django.conf import settings
from django.http import HttpRequest
from django.utils.functional import cached_property

from django_cloudflare.constants import DjangoCloudflareDefaultAttr
from django_cloudflare.constants import DjangoCloudflareHeader

__all__ = ["CloudflareMiddleware"]


@dataclasses.dataclass(frozen=True)
class HeaderConfiguration:
    is_enabled: bool
    key: DjangoCloudflareHeader
    attr_name: DjangoCloudflareDefaultAttr


class CloudflareMiddleware:
    def __init__(self, get_response: typing.Callable):
        self.get_response = get_response

    @cached_property
    def config(self) -> typing.Tuple[HeaderConfiguration, ...]:
        return (
            HeaderConfiguration(
                key=DjangoCloudflareHeader.cdn_loop,
                is_enabled=getattr(
                    settings, "CF_HEADER_CDN_LOOP_ENABLED", False
                ),
                attr_name=getattr(
                    settings,
                    "CF_HEADER_CDN_LOOP_ATTR_NAME",
                    DjangoCloudflareDefaultAttr.cf_cdn_loop,
                ),
            ),
            HeaderConfiguration(
                key=DjangoCloudflareHeader.ip,
                is_enabled=getattr(settings, "CF_HEADER_IP_ENABLED", False),
                attr_name=getattr(
                    settings,
                    "CF_HEADER_IP_ATTR_NAME",
                    DjangoCloudflareDefaultAttr.cf_ip,
                ),
            ),
            HeaderConfiguration(
                key=DjangoCloudflareHeader.country,
                is_enabled=getattr(
                    settings, "CF_HEADER_COUNTRY_ENABLED", False
                ),
                attr_name=getattr(
                    settings,
                    "CF_HEADER_COUNTRY_ATTR_NAME",
                    DjangoCloudflareDefaultAttr.cf_country,
                ),
            ),
            HeaderConfiguration(
                key=DjangoCloudflareHeader.ray,
                is_enabled=getattr(settings, "CF_HEADER_RAY_ENABLED", False),
                attr_name=getattr(
                    settings,
                    "CF_HEADER_RAY_ATTR_NAME",
                    DjangoCloudflareDefaultAttr.cf_ray,
                ),
            ),
            HeaderConfiguration(
                key=DjangoCloudflareHeader.warp_tag,
                is_enabled=getattr(
                    settings, "CF_HEADER_WARP_TAG_ENABLED", False
                ),
                attr_name=getattr(
                    settings,
                    "CF_HEADER_WARP_TAG_ATTR_NAME",
                    DjangoCloudflareDefaultAttr.cf_warp_tag,
                ),
            ),
        )

    def process_headers(self, request: HttpRequest) -> None:
        for header_config in self.config:
            if header_config.is_enabled:
                header_value = request.headers.get(header_config.key)
                setattr(request, header_config.attr_name, header_value)

    def __call__(self, request: HttpRequest) -> typing.Any:
        self.process_headers(request)
        return self.get_response(request)
