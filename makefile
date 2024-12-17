include common.mk

# Our directories
API_DIR = server
REQ_DIR = .
VENV_DIR = .venv


prod: 
	./run_local_server.sh

dev_env: 
	if [ ! -d $(VENV_DIR) ]; then python -m venv $(VENV_DIR); fi
	. $(VENV_DIR)/bin/activate
	pip install -r $(REQ_DIR)/requirements-dev.txt