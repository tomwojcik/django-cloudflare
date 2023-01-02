========
Settings
========

.. currentmodule:: django.conf.settings

For information about these headers, head over to Cloudflare documentation `HTTP request headers <https://developers.cloudflare.com/fundamentals/get-started/reference/http-request-headers/>`_.

.. attribute:: CF_HEADER_CDN_LOOP_ENABLED

Default: ``False``


If enabled, the value of ``Cdn-Loop`` header will be set on the request object.


.. attribute:: CF_HEADER_CDN_LOOP_ATTR_NAME


Default: ``cf_cdn_loop``


Allows you to define the attribute name that will allow you to access the previous value on the request object.

Example::

    request.cf_cdn_loop


.. attribute:: CF_HEADER_IP_ENABLED

Default: ``False``


If enabled, the value of ``Cf-Connecting-Ip`` header will be set on the request object.


.. attribute:: CF_HEADER_IP_ATTR_NAME


Default: ``cf_ip``


Allows you to define the attribute name that will allow you to access the previous value on the request object.

Example::

    request.cf_ip


.. attribute:: CF_HEADER_COUNTRY_ENABLED

Default: ``False``


If enabled, the value of ``Cf-Ipcountry`` header will be set on the request object.


.. attribute:: CF_HEADER_COUNTRY_ATTR_NAME


Default: ``cf_country``


Allows you to define the attribute name that will allow you to access the previous value on the request object.

Example::

    request.cf_country


.. attribute:: CF_HEADER_RAY_ENABLED

Default: ``False``


If enabled, the value of ``Cf-Ray`` header will be set on the request object.


.. attribute:: CF_HEADER_RAY_ATTR_NAME


Default: ``cf_ray``


Allows you to define the attribute name that will allow you to access the previous value on the request object.

Example::

    request.cf_ray


.. attribute:: CF_HEADER_WARP_TAG_ENABLED

Default: ``False``


If enabled, the value of ``Cf-Warp-Tag-Id`` header will be set on the request object.


.. attribute:: CF_HEADER_WARP_TAG_ATTR_NAME


Default: ``cf_warp_tag``


Allows you to define the attribute name that will allow you to access the previous value on the request object.

Example::

    request.cf_warp_tag
