PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black fibonacci/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy fibonacci/

ruff:
	$(PYTHON) -m ruff check fibonacci/
