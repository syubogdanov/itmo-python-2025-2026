PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black ipc/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy ipc/

ruff:
	$(PYTHON) -m ruff check ipc/
