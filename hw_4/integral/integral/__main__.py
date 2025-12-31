from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from enum import StrEnum, auto
from math import cos, pi
from os import cpu_count
from pathlib import Path

from integral.internal.integral import Integral


class ExecutorType(StrEnum):
    """The executor type."""

    PROCESS = auto()
    THREAD = auto()


@dataclass
class Measurement:
    """The measurement."""

    result: float
    time: timedelta
    n_jobs: int
    executor_type: ExecutorType

    def as_tuple(self) -> tuple[float, timedelta, int, ExecutorType]:
        """Return the measurement as a tuple."""
        return self.result, self.time, self.n_jobs, self.executor_type


def main() -> None:
    """Run the program."""
    measurements: list[Measurement] = []

    integral = Integral(cos)
    a = 0.0
    b = pi / 2

    cpu_num = cpu_count() or 1
    for n_jobs in range(1, cpu_num * cpu_num + 1):
        process_pool_executor = ProcessPoolExecutor(max_workers=n_jobs)
        thread_pool_executor = ThreadPoolExecutor(max_workers=n_jobs)

        t1_1 = datetime.now(UTC)
        r1 = integral.estimate(a, b, n_jobs=n_jobs, executor=process_pool_executor)
        t1_2 = datetime.now(UTC)

        t2_1 = datetime.now(UTC)
        r2 = integral.estimate(a, b, n_jobs=n_jobs, executor=thread_pool_executor)
        t2_2 = datetime.now(UTC)

        dt1 = t1_2 - t1_1
        dt2 = t2_2 - t2_1

        m1 = Measurement(result=r1, time=dt1, n_jobs=n_jobs, executor_type=ExecutorType.PROCESS)
        m2 = Measurement(result=r2, time=dt2, n_jobs=n_jobs, executor_type=ExecutorType.THREAD)

        measurements.append(m1)
        measurements.append(m2)

    measurements.sort(key=lambda m: m.time)

    with Path("measurements.csv").open(mode="w") as file:
        print("result", "time", "n_jobs", "executor_type", sep=",", file=file)
        for measurement in measurements:
            print(*measurement.as_tuple(), sep=",", file=file)


if __name__ == "__main__":
    main()
