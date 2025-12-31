from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from enum import StrEnum, auto
from multiprocessing import Process
from pathlib import Path
from threading import Thread

from fibonacci.internal.fibonacci import fibonacci


def parse_args() -> tuple[int, int]:
    """Parse the command line arguments."""
    parser = ArgumentParser("fibonacci")

    parser.add_argument("--n", type=int, default=1_000_000)
    parser.add_argument("--cpu-num", type=int, default=10)

    args = parser.parse_args()
    return args.n, args.cpu_num


class ParallelismType(StrEnum):
    """The parallelism type."""

    NONE = auto()
    PROCESS = auto()
    THREAD = auto()


@dataclass
class Measurement:
    """The measurement."""

    time: timedelta
    parallelism: ParallelismType

    def as_tuple(self) -> tuple[timedelta, ParallelismType]:
        """Return the measurement as a tuple."""
        return self.time, self.parallelism


def synchronous(n: int, cpu_num: int) -> Measurement:
    """Make a synchronous measurement."""
    started_at = datetime.now(UTC)

    for _ in range(cpu_num):
        fibonacci(n)

    finished_at = datetime.now(UTC)
    time = finished_at - started_at

    return Measurement(time, ParallelismType.NONE)


def threading(n: int, cpu_num: int) -> Measurement:
    """Make a threading measurement."""
    started_at = datetime.now(UTC)

    threads = [Thread(target=fibonacci, args=(n,)) for _ in range(cpu_num)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    finished_at = datetime.now(UTC)
    time = finished_at - started_at

    return Measurement(time, ParallelismType.THREAD)


def multiprocessing(n: int, cpu_num: int) -> Measurement:
    """Make a multiprocessing measurement."""
    started_at = datetime.now(UTC)

    processes = [Process(target=fibonacci, args=(n,)) for _ in range(cpu_num)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    finished_at = datetime.now(UTC)
    time = finished_at - started_at

    return Measurement(time, ParallelismType.PROCESS)


def main() -> None:
    """Run the program."""
    n, cpu_num = parse_args()

    measurements = [
        synchronous(n, cpu_num),
        threading(n, cpu_num),
        multiprocessing(n, cpu_num),
    ]

    measurements.sort(key=lambda m: m.time)

    with Path("measurements.csv").open(mode="w") as file:
        print("time", "parallelism", sep=",", file=file)
        for measurement in measurements:
            print(*measurement.as_tuple(), sep=",", file=file)


if __name__ == "__main__":
    main()
