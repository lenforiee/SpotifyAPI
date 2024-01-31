shell:
	poetry env use 3.9
	poetry install --with dev
	poetry shell

lint:
	poetry run pre-commit run --all-files
