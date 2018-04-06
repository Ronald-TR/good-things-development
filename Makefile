setup:
	pip install pipenv
	pipenv install
	pipenv install --dev
	$(shell export PYTHONPATH=$PYTHONPATH:$(pwd))

test:
	python tests/tests.py

codacy:
	pylama

