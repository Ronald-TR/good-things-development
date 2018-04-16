setup:
	pip install pipenv
	pipenv install
	pipenv install --dev

test:	
	python tests/tests.py

codacy:
	pylama

env:
	@export PYTHONPATH=${PYTHONPATH}
	@echo ${PYTHONPATH};
