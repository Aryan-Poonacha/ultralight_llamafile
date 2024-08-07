install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m unittest tests/*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py

	#ruff linting is 10-100X faster than pylint
	ruff check *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

#replace xxx with the .py (without the .py) file that you want to run
deploy:
	python -m main

#if u want a different run file that's different from deploy
run:
	python -m main
		
all: install lint test format deploy
