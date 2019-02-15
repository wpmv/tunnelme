.PHONY: clean clean-build clean-pyc clean-test lint test test-all coverage requirements docs dist install all

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "requirements - generate requirements from .in files"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "dist - package"

requirements/main.txt: requirements/main.in
	pip install --upgrade pip
	pip install --upgrade pip-tools
	pip-compile requirements/main.in

requirements/dev.txt: requirements/dev.in
	pip install --upgrade pip
	pip install --upgrade pip-tools
	pip-compile requirements/dev.in

requirements: requirements/main.txt requirements/dev.txt

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:
	flake8 health_check tests

test:
	pytest

test-all:
	tox

coverage:
	coverage run --source tunnel_utils setup.py test
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs:
	rm -f docs/tunnel_utils.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ tunnel_utils
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

all: dist docs test
