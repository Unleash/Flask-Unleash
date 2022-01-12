SHELL := /bin/bash
ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = flask_unleash

#-----------------------------------------------------------------------
# Rules of Rules : Grouped rules that _doathing_
#-----------------------------------------------------------------------
test: lint pytest

precommit: clean generate-requirements

build: clean build-package upload

build-local: clean build-package

#-----------------------------------------------------------------------
# Install
#-----------------------------------------------------------------------

install:
	pip install -U -r requirements.txt && \
	python setup.py install

#-----------------------------------------------------------------------
# Testing & Linting
#-----------------------------------------------------------------------
lint:
	pylint ${PROJECT_NAME} && \
	mypy ${PROJECT_NAME};

pytest:
	export PYTHONPATH=${ROOT_DIR}:$$PYTHONPATH && \
	py.test --cov ${PROJECT_NAME} tests

tox-osx:
	tox -c tox-osx.ini --parallel auto

#-----------------------------------------------------------------------
# Rules
#-----------------------------------------------------------------------
clean:
	rm -rf build; \
	rm -rf dist;

build-package:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*


#-----------------------------------------------------------------------
# Run demo app
#-----------------------------------------------------------------------
run:
	export PYTHONPATH=${ROOT_DIR}; \
	python demo_app/app.py

run-gunicorn:
    export PYTHONPATH=${ROOT_DIR}; \
	gunicorn --config gunicorn_config.py wsgi