PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black integral/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy integral/

ruff:
	$(PYTHON) -m ruff check integral/
