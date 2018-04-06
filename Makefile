setup:
	pip install pipenv
	pipenv install
	pipenv install --dev

test:
	$(shell export PYTHONPATH=$PYTHONPATH:$(pwd))
	python tests/tests.py

codacy:
	pylama

