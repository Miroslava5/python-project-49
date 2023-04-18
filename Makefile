install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even
	
brain-calc:
	poetry run brain-calc

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

make lint:
	poetry run flake8 Brain_games
