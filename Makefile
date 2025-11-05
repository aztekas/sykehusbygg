.PHONY: help sync test lint format typecheck clean ensure-clean-git

ensure-clean-git:
	@echo "Checking for clean git working tree..."
	@if ! git diff --quiet || ! git diff --cached --quiet; then \
		echo "Error: working tree not clean. Commit or stash changes before running 'make lint' or 'make format'."; \
		exit 1; \
	fi

help:
	@echo "Usage: make <target>"
	@echo "Common targets:"
	@echo "  sync                - create/update .venv and install dev deps (uses uv)"
	@echo "  test                - run pytest (uses uv-runner)"
	@echo "  lint                - run ruff (with --fix) over src and tests"
	@echo "  lint-and-commit     - run lint, then commit fixes if any (requires clean git tree)"
	@echo "  ci-lint             - run ruff in CI style (no --fix)"
	@echo "  format              - format code (uses ruff/black via uv)"
	@echo "  format-and-commit   - format then commit fixes if any (requires clean git tree)"
	@echo "  ci-format           - check formatting (CI mode)"
	@echo "  lft                 - run sync, lint-and-commit and format-and-commit (dev convenience)"
	@echo "  typecheck           - run mypy (currently commented out)"
	@echo "  clean               - remove python build/test artifacts and .venv (commented out)"
	@echo "  ensure-clean-git    - helper: fail if git working tree has uncommitted changes"
	@echo "Examples:"
	@echo "  make sync"
	@echo "  make test"
	@echo "  make lint-and-commit"

sync:
	@echo "Syncing dependencies with uv..."
	uv sync

test: sync
	@echo "Running tests..."
	uv run pytest

lint:
	@echo "Running ruff linter with fix..."
	uv run ruff check src tests --fix

lint-and-commit: ensure-clean-git lint
	@echo "Committing ruff linter fixes if any..."
	@git diff --quiet || git commit -am "Apply Ruff linter fixes"

ci-lint:
	@echo "Running ruff linter (CI mode)"
	uv run ruff check src tests

format:
	@echo "Running ruff black formatting"
	uv run ruff format src tests

format-and-commit: ensure-clean-git format
	@echo "Committing ruff black formatting fixes if any..."
	@git diff --quiet || git commit -am "Apply Ruff black formatting fixes"

ci-format:
	@echo "Running ruff black formatting (CI mode)"
	uv run ruff format --check src tests

lft: sync ensure-clean-git lint-and-commit format-and-commit
	@echo " -> Skipping typecheck for now"

# typecheck: sync
# 	@echo "Running mypy..."
# 	$(PY) -m mypy src

# clean:
# 	@echo "Cleaning python build/test artifacts..."
# 	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist .venv
