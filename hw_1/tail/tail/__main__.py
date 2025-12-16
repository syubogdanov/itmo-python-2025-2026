import sys

from argparse import ArgumentParser
from collections import deque
from pathlib import Path
from typing import TextIO


def tail(file: TextIO, *, n: int = 10, name: str | None = None) -> None:
    """Display the last part of a file."""
    buffer: deque[str] = deque(maxlen=n)

    for line in file:
        buffer.append(line)

    if name:
        line = f"==> {name} <==\n"
        sys.stdout.write(line)

    for line in buffer:
        sys.stdout.write(line)

    if name:
        sys.stdout.write("\n")


def main() -> None:
    """Run the program."""
    parser = ArgumentParser(prog="tail", description="tail -- display the last part of a file")
    parser.add_argument("file", nargs="*", type=Path, help="file to read (default: stdin)")

    args = parser.parse_args()

    try:
        if not args.file:
            tail(sys.stdin, n=17)

        for path in args.file:
            name = path.as_posix() if len(args.file) > 1 else None
            with path.open() as file:
                tail(file, name=name)

    except Exception as exception:
        detail = str(exception)
        parser.error(detail)

    except KeyboardInterrupt:
        parser.exit(status=2)


if __name__ == "__main__":
    main()
