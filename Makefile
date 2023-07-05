install:
	poetry install --only main

build: install
	poetry build

dev-install:
	poetry install

lint: dev-install
	poetry run mypy --verbose anymusic
	poetry run pylint --verbose anymusic

format: dev-install
	poetry run black --verbose anymusic example

docs: dev-install
	poetry run mkdocs serve

build-docs: dev-install
	poetry run mkdocs build

.PHONY: install build dev-install lint format docs build-docs
