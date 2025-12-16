import sys

from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path
from typing import TextIO


@dataclass
class Statistics:
    """The statistics."""

    lines: int = 0
    words: int = 0
    chars: int = 0

    def __add__(self, other: "Statistics") -> "Statistics":
        """Sum the statistics."""
        return Statistics(
            lines=self.lines + other.lines,
            words=self.words + other.words,
            chars=self.chars + other.chars,
        )

    def __repr__(self) -> str:
        """Show the statistics."""
        return f"{self.lines:>8} {self.words:>8} {self.chars:>8}"

    def print(self, *, name: str | None = None) -> None:
        """Print the statistics."""
        sys.stdout.write(repr(self))
        if name:
            sys.stdout.write(" ")
            sys.stdout.write(name)
        sys.stdout.write("\n")


def wc(file: TextIO) -> Statistics:
    """Return the statistics."""
    statistics = Statistics()

    for line in file:
        statistics.lines += 1
        statistics.words += len(line.split())
        statistics.chars += len(line)

    return statistics


def main() -> int:
    """Run the program."""
    parser = ArgumentParser(prog="wc", description="wc -- word, line, character, and byte count")
    parser.add_argument("file", nargs="*", type=Path, help="file to read (default: stdin)")

    args = parser.parse_args()

    try:
        if not args.file:
            statistics = wc(sys.stdin)
            statistics.print()

        total = Statistics()

        for path in args.file:
            with path.open() as file:
                statistics = wc(file)
                statistics.print(name=path.as_posix())
                total += statistics

        if len(args.file) > 1:
            total.print(name="total")

    except Exception as exception:
        detail = str(exception)
        parser.error(detail)

    except KeyboardInterrupt:
        parser.exit(status=2)


if __name__ == "__main__":
    main()
