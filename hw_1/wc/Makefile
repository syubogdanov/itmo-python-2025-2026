PYTHON = python -m


# Formatters
format: black

black:
	$(PYTHON) black wc/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) mypy wc/

ruff:
	$(PYTHON) ruff check wc/
