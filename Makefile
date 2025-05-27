# Consistent set of make tasks.
.DEFAULT_GOAL:=help  # because it's is a safe task.

clean: # Remove the environment.
	rm -rf .venv
	rm -rf *.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

docs: # Build the documentation.
	cd docs && mkdocs build

docs-serve: # Serve the documention.
	cd docs && mkdocs serve

lint:  # Lint the code with ruff.
	.venv/bin/ruff check ./src ./tests

lock:  # Create or update the requirements file.
	uv lock

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

report:  # Report the python version and pip list.
	.venv/bin/python --version
	uv pip list -v

test:  # Run tests.
	.venv/bin/pytest ./tests --verbose --color=yes
	.venv/bin/pytest --cov=src

venv:  # Create the virtual environment.
	uv venv .venv
	uv sync 

