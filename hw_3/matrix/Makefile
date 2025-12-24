PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black matrix/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy matrix/

ruff:
	$(PYTHON) -m ruff check matrix/
