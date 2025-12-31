def fibonacci(n: int) -> int:
    """Return the ``n``-th Fibonacci number."""
    if n < 0:
        detail = "'n' must be non-negative"
        raise ValueError(detail)

    if n == 0:
        return 0

    a = 1
    b = 1

    for _ in range(2, n):
        a, b = b, a + b

    return b
