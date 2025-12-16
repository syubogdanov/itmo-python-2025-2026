PYTHON = python


# Formatters
format: black

black:
	$(PYTHON) -m black tail/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) -m mypy tail/

ruff:
	$(PYTHON) -m ruff check tail/
