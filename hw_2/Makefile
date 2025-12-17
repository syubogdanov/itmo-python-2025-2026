PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black latex/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy latex/

ruff:
	$(PYTHON) -m ruff check latex/
