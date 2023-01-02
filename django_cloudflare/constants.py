import enum


class DjangoCloudflareHeader(str, enum.Enum):
    cdn_loop = "Cdn-Loop"
    ip = "Cf-Connecting-Ip"
    country = "Cf-Ipcountry"
    ray = "Cf-Ray"
    warp_tag = "Cf-Warp-Tag-Id"


class DjangoCloudflareDefaultAttr(str, enum.Enum):
    cf_cdn_loop = "cf_cdn_loop"
    cf_ip = "cf_ip"
    cf_country = "cf_country"
    cf_ray = "cf_ray"
    cf_warp_tag = "cf_warp_tag"
