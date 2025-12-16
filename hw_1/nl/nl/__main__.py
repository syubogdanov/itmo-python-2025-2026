import sys

from argparse import ArgumentParser
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from typing import TextIO


@contextmanager
def maybe_open(path: Path | None, encoding: str = "utf-8") -> Generator[TextIO]:
    """Open a file or return ``sys.stdin``."""
    if path is None:
        yield sys.stdin
        return
    with path.open(encoding=encoding) as file:
        yield file


def main() -> None:
    """Run the program."""
    parser = ArgumentParser(prog="nl", description="nl -- line numbering filter")
    parser.add_argument("file", nargs="?", type=Path, help="file to read (default: stdin)")

    args = parser.parse_args()

    try:
        with maybe_open(args.file) as file:
            for lineno, line in enumerate(file, start=1):
                sys.stdout.write(f"{lineno:6d}  {line}")

    except Exception as exception:
        detail = str(exception)
        parser.error(detail)

    except KeyboardInterrupt:
        parser.exit(status=2)


if __name__ == "__main__":
    main()
