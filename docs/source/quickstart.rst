==========
Quickstart
==========

************
Installation
************

Install the package from PYPI

.. code-block:: bash

   $ pip install -U django-cloudflare

Add :py:class:`django_cloudflare.CloudflareMiddleware` to your middlewares.

``settings.py``::

    MIDDLEWARE += ["django_cloudflare.CloudflareMiddleware"]

    # example configuration, all headers are disabled by default
    CF_HEADER_IP_ENABLED = True

For details about the configuration, see :doc:`settings <settings>` page.

**********
How to use
**********

If you used the configuration above and the request was proxied via Cloudflare, you could then access the ip like this ``request.cf_ip``.
