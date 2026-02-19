venv:
	uv venv

install: venv
	uv sync --group dev
	uv run pre-commit install

test:
	uv run pytest

lint:
	uv run pre-commit run --all-files

clean:
	rm -rf .venv .pytest_cache .ruff_cache __pycache__ site
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
