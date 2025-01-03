# common variables
PYTHONFILES = $(shell ls *.py)
PYTESTFLAGS = -vv --verbose --cov-config=.coveragerc --cov=app tests/

# Our directories
API_DIR = app
REQ_DIR = .
VENV_DIR = .venv


prod: tests
	./run_local_server.sh

tests: dev_env pytests

dev_env: 
	if [ ! -d $(VENV_DIR) ]; then python -m venv $(VENV_DIR); fi
	. $(VENV_DIR)/bin/activate
	pip install -r $(REQ_DIR)/requirements-dev.txt

lint: $(patsubst %.py,%.pylint,$(PYTHONFILES))

%.pylint:
	$(LINTER) $(PYLINTFLAGS) $*.py

pytests: 
	pytest $(PYTESTFLAGS) --cov=$(PKG)
	coverage html

clean:
	rm -rf .pytest_cache
	rm -rf coverage_html_report