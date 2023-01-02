try:
    # see https://tomwojcik.com/posts/2023-01-02/python-311-str-enum-breaking-change/  # noqa: E501
    from enum import StrEnum
except ImportError:  # pragma: no cover
    from enum import Enum  # pragma: no cover

    class StrEnum(str, Enum):  # pragma: no cover
        pass  # pragma: no cover


class DjangoCloudflareHeader(StrEnum):
    cdn_loop = "Cdn-Loop"
    ip = "Cf-Connecting-Ip"
    country = "Cf-Ipcountry"
    ray = "Cf-Ray"
    warp_tag = "Cf-Warp-Tag-Id"


class DjangoCloudflareDefaultAttr(StrEnum):
    cf_cdn_loop = "cf_cdn_loop"
    cf_ip = "cf_ip"
    cf_country = "cf_country"
    cf_ray = "cf_ray"
    cf_warp_tag = "cf_warp_tag"
