# Change Log

This document records all notable changes to django-cloudflare.
This project adheres to [Semantic Versioning](http://semver.org/).

Latest release

## `1.0.0`

*Release date: Feb 2026*

- Drop Python 3.8, 3.9 support. Minimum Python version is now 3.10.
- Drop Django 3.x, 4.0, 4.1 support. Minimum Django version is now 4.2.
- Add Django 5.1, 5.2, and 6.0 support.
- Add async middleware support (Django 4.2+ async-capable middleware).
- Replace black, isort, flake8 with ruff.
- Modernize CI with GitHub Actions trusted publishers (OIDC).
- Replace coverage+manage.py test with pytest+pytest-django.

## `0.0.1`

*Release date: Jul 2023*

- Initial release.

[1.0.0]: https://github.com/tomwojcik/django-cloudflare/compare/v0.0.1...v1.0.0
