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

deploy:
	python -m main

#if u want a different run file that's different from deploy
run:
	python -m main

IMAGE_NAME = irevia/llamafile_chatbot_app
VERSION = latest

build:
	docker build -t $(IMAGE_NAME):$(VERSION) .

push:
	docker push $(IMAGE_NAME):$(VERSION)

all: install lint test format deploy build push