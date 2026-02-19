[![Build Status](https://github.com/tomwojcik/django-cloudflare/workflows/CI/badge.svg)](https://github.com/tomwojcik/django-cloudflare/actions/workflows/ci.yml)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-cloudflare.svg)](https://pypi.org/project/django-cloudflare/)
[![Latest Version](https://img.shields.io/pypi/v/django-cloudflare.svg)](https://pypi.org/project/django-cloudflare/)
[![Docs](https://readthedocs.org/projects/django-cloudflare/badge/?version=latest)](https://django-cloudflare.readthedocs.io/en/latest/)

# django-cloudflare

A reusable Django middleware that allows you to easily extract Cloudflare headers from incoming requests.

Resources:

* **Source**: https://github.com/tomwojcik/django-cloudflare
* **Documentation**: https://django-cloudflare.readthedocs.io/
* **Changelog**: https://django-cloudflare.readthedocs.io/en/latest/changelog/

## Supported headers

| Cloudflare header | Default attribute | Setting to enable |
|---|---|---|
| `Cdn-Loop` | `request.cf_cdn_loop` | `CF_HEADER_CDN_LOOP_ENABLED` |
| `Cf-Connecting-Ip` | `request.cf_ip` | `CF_HEADER_IP_ENABLED` |
| `Cf-Connecting-Ipv6` | `request.cf_ipv6` | `CF_HEADER_IPV6_ENABLED` |
| `Cf-Ipcountry` | `request.cf_country` | `CF_HEADER_COUNTRY_ENABLED` |
| `Cf-Ray` | `request.cf_ray` | `CF_HEADER_RAY_ENABLED` |
| `Cf-Visitor` | `request.cf_visitor` | `CF_HEADER_VISITOR_ENABLED` |
| `Cf-Warp-Tag-Id` | `request.cf_warp_tag` | `CF_HEADER_WARP_TAG_ENABLED` |
| `X-Forwarded-For` | `request.cf_forwarded_for` | `CF_HEADER_FORWARDED_FOR_ENABLED` |
| `X-Forwarded-Proto` | `request.cf_forwarded_proto` | `CF_HEADER_FORWARDED_PROTO_ENABLED` |

All headers are disabled by default. Each attribute name can be customized via the corresponding `*_ATTR_NAME` setting.

## Installation

```bash
pip install -U django-cloudflare
```

## Usage

Add the middleware and enable the headers you need in your `settings.py`:

```python
MIDDLEWARE += ["django_cloudflare.CloudflareMiddleware"]

CF_HEADER_IP_ENABLED = True
CF_HEADER_COUNTRY_ENABLED = True
```

Then access the values on the request object:

```python
def my_view(request):
    ip = request.cf_ip
    country = request.cf_country
```

Both sync and async views are supported.

## Requirements

Python 3.10+, Django 4.2+
