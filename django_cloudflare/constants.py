import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:  # pragma: no cover
    from enum import Enum

    class StrEnum(str, Enum):
        pass


class DjangoCloudflareHeader(StrEnum):
    cdn_loop = "Cdn-Loop"
    ip = "Cf-Connecting-Ip"
    ipv6 = "Cf-Connecting-Ipv6"
    country = "Cf-Ipcountry"
    ray = "Cf-Ray"
    visitor = "Cf-Visitor"
    warp_tag = "Cf-Warp-Tag-Id"
    forwarded_for = "X-Forwarded-For"
    forwarded_proto = "X-Forwarded-Proto"


class DjangoCloudflareDefaultAttr(StrEnum):
    cf_cdn_loop = "cf_cdn_loop"
    cf_ip = "cf_ip"
    cf_ipv6 = "cf_ipv6"
    cf_country = "cf_country"
    cf_ray = "cf_ray"
    cf_visitor = "cf_visitor"
    cf_warp_tag = "cf_warp_tag"
    cf_forwarded_for = "cf_forwarded_for"
    cf_forwarded_proto = "cf_forwarded_proto"
