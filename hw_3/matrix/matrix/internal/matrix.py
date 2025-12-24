from __future__ import annotations

import json
import random

from numbers import Integral
from typing import TYPE_CHECKING, Any, Self

from matrix.internal.mixins import CachedNDArrayOperatorsMixin


if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import TextIO

    from numpy import ufunc as ufunc_t


class Matrix[T: Integral](CachedNDArrayOperatorsMixin):
    """The matrix."""

    __slots__ = ("_arrays",)

    def __init__(self, iterables: Iterable[Iterable[T]], /) -> None:
        """Initialize the object."""
        if not (iterables := list(iterables)):
            detail = "'n' must be positive"
            raise ValueError(detail)

        n = len(iterables)
        arrays: list[list[T]] = [[] for _ in range(n)]

        try:
            for column in zip(*iterables, strict=True):
                for index, item in enumerate(column):
                    arrays[index].append(item)

        except ValueError:
            detail = "all rows must have the same length"
            raise ValueError(detail) from None

        if not arrays[0]:
            detail = "'m' must be positive"
            raise ValueError(detail)

        self._arrays = tuple(tuple(array) for array in arrays)

    @property
    def shape(self) -> tuple[int, int]:
        """Return the matrix shape."""
        n = len(self._arrays)
        m = len(self._arrays[0])
        return n, m

    def __array_ufunc__(
        self,
        ufunc: ufunc_t,
        method: str,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """Применить функцию к матрице."""
        arrays: list[Any] = []

        for arg in args:
            array = arg.json() if isinstance(arg, Matrix) else arg
            arrays.append(array)

        ndarray = ufunc(*arrays, **kwargs)
        return Matrix(ndarray)

    def __getitem__(self, index: int, /) -> tuple[T, ...]:
        """Return the row."""
        return self._arrays[index]

    def __len__(self) -> int:
        """Return the length."""
        return len(self._arrays)

    def __hash__(self) -> int:
        """Return the hash."""
        return hash(self._arrays)

    def __str__(self) -> str:
        """Represent as a string."""
        items = [[str(item) for item in array] for array in self._arrays]
        width = max(len(item) for array in items for item in array)
        return "\n".join(" ".join(item.rjust(width) for item in array) for array in items)

    def dump(self, fd: TextIO, /, **kwargs: Any) -> None:
        """Dump the matrix to the file."""
        json.dump(self._arrays, fd, **kwargs)

    def json(self) -> list[list[T]]:
        """Return the matrix as a JSON."""
        return [list(array) for array in self._arrays]

    @classmethod
    def load(cls, fd: TextIO, /, **kwargs: Any) -> Self:
        """Load the matrix from the file."""
        return cls(json.load(fd, **kwargs))

    @classmethod
    def randint(cls, *, n: int = 10, m: int = 10, a: int = 0, b: int = 10) -> Self:
        """Return a matrix ``x``, where ``x.shape == (n, m)`` and ``a <= x[i, j] <= b``."""
        return cls((random.randint(a, b) for _ in range(m)) for _ in range(n))
