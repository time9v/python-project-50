install:
	poetry install

test:
	poetry run pytest


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 gendiff


test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml


selfcheck:
	poetry check


check: selfcheck test lint
