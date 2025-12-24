from collections.abc import Callable, Hashable
from functools import wraps
from typing import TypeVar


H = TypeVar("H", bound=Hashable)
R = TypeVar("R")


def binary_operator(binop: Callable[[H, H], R], /, *, maxsize: int = 32) -> Callable[[H, H], R]:
    """Cache the binary operator."""
    if maxsize <= 0:
        detail = "'maxsize' must be positive"
        raise ValueError(detail)

    cache: dict[tuple[H, H], R] = {}

    @wraps(binop)
    def wrapper(lhs: H, rhs: H) -> R:
        """Wrap the operator."""
        key = (lhs, rhs)
        if key in cache:
            return cache[key]

        result = binop(lhs, rhs)

        if len(cache) >= maxsize:
            key = next(iter(cache))
            del cache[key]

        cache[key] = result
        return result

    return wrapper


def unary_operator(unop: Callable[[H], R], /) -> Callable[[H], R]:
    """Cache the unary operator."""
    cache: dict[H, R] = {}

    @wraps(unop)
    def wrapper(item: H) -> R:
        """Wrap the operator."""
        if item in cache:
            return cache[item]

        result = unop(item)
        cache[item] = result

        return result

    return wrapper
