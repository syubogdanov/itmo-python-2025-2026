PYTHON = python -m


# Formatters
format: black

black:
	$(PYTHON) black nl/


# Linters
lint: ruff mypy

mypy:
	$(PYTHON) mypy nl/

ruff:
	$(PYTHON) ruff check nl/
