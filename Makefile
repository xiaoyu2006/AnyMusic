install:
	poetry install --only main

dev-install:
	poetry install

lint: dev-install
	poetry run mypy anymusic
	poetry run pylint anymusic

format: dev-install
	poetry run black anymusic example

.PHONY: install dev-install lint
