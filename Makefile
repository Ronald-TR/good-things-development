setup:
	pip install pipenv
	pipenv --python=python3
	pipenv install
	pipenv install --dev

test:
	python testcases/tests.py

codacy:
	python pylama

