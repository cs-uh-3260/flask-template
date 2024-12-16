include common.mk

# Our directories
API_DIR = server
DB_DIR = data
REQ_DIR = .
VENV_DIR = .venv


prod: all_tests
	./local.sh

all_tests: 
	cd $(API_DIR); make tests
	cd $(DB_DIR); make tests

dev_env: 
	if [ ! -d $(VENV_DIR) ]; then python -m venv $(VENV_DIR); fi
	. $(VENV_DIR)/bin/activate
	pip install -r $(REQ_DIR)/requirements-dev.txt
	export PYTHON_PATH=$(shell pwd)

docs:
	cd $(API_DIR); make docs
