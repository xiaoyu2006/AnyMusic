install:
	poetry install --no-dev

dev-install:
	poetry install

lint: dev-install
	poetry run mypy anymusic
	poetry run pylint anymusic

.PHONY: install dev-install lint
