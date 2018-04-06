setup:
	pip install pipenv
	pipenv --python=python3
	pipenv install
	pipenv install --dev
	export PYTHONPATH=`pwd`

test:
	python tests/tests.py

codacy:
	pylama

