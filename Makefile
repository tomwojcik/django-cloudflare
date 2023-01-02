test:
	poetry run coverage run --source='django_cloudflare' manage.py test tests
	poetry run coverage report
