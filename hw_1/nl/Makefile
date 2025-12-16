PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black nl/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy nl/

ruff:
	$(PYTHON) -m ruff check nl/
