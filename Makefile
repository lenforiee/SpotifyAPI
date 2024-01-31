# To release a new version `make release ver=<args>`
# https://python-poetry.org/docs/cli/#version

CURRENT_BRANCH := $(shell git branch --show-current)


shell:
	poetry env use 3.9
	poetry install --with dev
	poetry shell


release:
	$(if $(filter $(CURRENT_BRANCH),main),,$(error ERR: Not on main branch))
	$(eval VERSION := $(shell poetry version $(ver) -s))
	git add pyproject.toml
	git commit -m "v$(VERSION)"
	git tag v$(VERSION)
	git push
	git push --tags
	poetry version

release-dry:
	$(if $(filter $(CURRENT_BRANCH),main),,$(warning WARN: Not on main branch))
	$(eval VERSION := $(shell poetry version $(ver) -s --dry-run))
	@echo "Dry run: git add pyproject.toml"
	@echo "Dry run: git tag v$(VERSION)"
	@echo "Dry run: git push"
	@echo "Dry run: git push --tags"
	@echo "Run `make release ver=$(ver)` to release"

lint:
	poetry run pre-commit run --all-files

test:
	poetry run mypy
