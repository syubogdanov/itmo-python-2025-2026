PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black wc/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy wc/

ruff:
	$(PYTHON) -m ruff check wc/
