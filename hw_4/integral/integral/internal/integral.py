from collections.abc import Callable
from concurrent.futures import Executor, Future
from dataclasses import dataclass
from math import ceil, isclose


@dataclass
class Integral:
    """The integral."""

    f: Callable[[float], float]

    def estimate(
        self,
        a: float,
        b: float,
        *,
        n_iter: int = 10_000_000,
        n_jobs: int = 1,
        executor: Executor | None = None,
    ) -> float:
        """Estimate the integral."""
        if n_iter <= 0:
            detail = "'n_iter' must be positive"
            raise ValueError(detail)

        if n_jobs <= 0:
            detail = "'n_jobs' must be positive"
            raise ValueError(detail)

        if isclose(a, b):
            return 0.0

        if executor is None:
            return self._estimate(a, b, n_iter=n_iter)

        per_job = (b - a) / n_jobs
        n_iter0 = ceil(n_iter / n_jobs)

        futures: list[Future[float]] = []

        for chunk in range(n_jobs):
            a0 = a + chunk * per_job
            b0 = a0 + per_job

            future = executor.submit(self._estimate, a0, b0, n_iter=n_iter0)
            futures.append(future)

        return sum(future.result() for future in futures)

    def _estimate(self, a: float, b: float, *, n_iter: int) -> float:
        """Estimate the integral."""
        accumulator = 0.0
        dx = (b - a) / n_iter

        for chunk in range(n_iter):
            x = a + chunk * dx
            accumulator += self.f(x) * dx

        return accumulator
