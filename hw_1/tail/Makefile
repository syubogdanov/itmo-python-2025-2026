PYTHON = python -m


# Formatters
format: black

black:
	$(PYTHON) black tail/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) mypy tail/

ruff:
	$(PYTHON) ruff check tail/
