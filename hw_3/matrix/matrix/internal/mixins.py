from numpy.lib.mixins import NDArrayOperatorsMixin

from matrix.internal import cache


class CachedNDArrayOperatorsMixin(NDArrayOperatorsMixin):
    """Cached ``NDArrayOperatorsMixin``."""

    __slots__ = ()

    __hash__ = NDArrayOperatorsMixin.__hash__

    __lt__ = cache.binary_operator(NDArrayOperatorsMixin.__lt__)
    __le__ = cache.binary_operator(NDArrayOperatorsMixin.__le__)
    __eq__ = cache.binary_operator(NDArrayOperatorsMixin.__le__)
    __ne__ = cache.binary_operator(NDArrayOperatorsMixin.__le__)
    __gt__ = cache.binary_operator(NDArrayOperatorsMixin.__le__)
    __ge__ = cache.binary_operator(NDArrayOperatorsMixin.__le__)

    __add__ = cache.binary_operator(NDArrayOperatorsMixin.__add__)
    __radd__ = cache.binary_operator(NDArrayOperatorsMixin.__radd__)
    __iadd__ = cache.binary_operator(NDArrayOperatorsMixin.__iadd__)

    __sub__ = cache.binary_operator(NDArrayOperatorsMixin.__sub__)
    __rsub__ = cache.binary_operator(NDArrayOperatorsMixin.__rsub__)
    __isub__ = cache.binary_operator(NDArrayOperatorsMixin.__isub__)

    __mul__ = cache.binary_operator(NDArrayOperatorsMixin.__mul__)
    __rmul__ = cache.binary_operator(NDArrayOperatorsMixin.__rmul__)
    __imul__ = cache.binary_operator(NDArrayOperatorsMixin.__imul__)

    __matmul__ = cache.binary_operator(NDArrayOperatorsMixin.__matmul__)
    __rmatmul__ = cache.binary_operator(NDArrayOperatorsMixin.__rmatmul__)
    __imatmul__ = cache.binary_operator(NDArrayOperatorsMixin.__imatmul__)

    __truediv__ = cache.binary_operator(NDArrayOperatorsMixin.__truediv__)
    __rtruediv__ = cache.binary_operator(NDArrayOperatorsMixin.__rtruediv__)
    __itruediv__ = cache.binary_operator(NDArrayOperatorsMixin.__itruediv__)

    __floordiv__ = cache.binary_operator(NDArrayOperatorsMixin.__floordiv__)
    __rfloordiv__ = cache.binary_operator(NDArrayOperatorsMixin.__rfloordiv__)
    __ifloordiv__ = cache.binary_operator(NDArrayOperatorsMixin.__ifloordiv__)

    __mod__ = cache.binary_operator(NDArrayOperatorsMixin.__mod__)
    __rmod__ = cache.binary_operator(NDArrayOperatorsMixin.__rmod__)
    __imod__ = cache.binary_operator(NDArrayOperatorsMixin.__imod__)

    __divmod__ = cache.binary_operator(NDArrayOperatorsMixin.__divmod__)
    __rdivmod__ = cache.binary_operator(NDArrayOperatorsMixin.__rdivmod__)

    __pow__ = cache.binary_operator(NDArrayOperatorsMixin.__pow__)
    __rpow__ = cache.binary_operator(NDArrayOperatorsMixin.__rpow__)
    __ipow__ = cache.binary_operator(NDArrayOperatorsMixin.__ipow__)

    __lshift__ = cache.binary_operator(NDArrayOperatorsMixin.__lshift__)
    __rlshift__ = cache.binary_operator(NDArrayOperatorsMixin.__rlshift__)
    __ilshift__ = cache.binary_operator(NDArrayOperatorsMixin.__ilshift__)

    __rshift__ = cache.binary_operator(NDArrayOperatorsMixin.__rshift__)
    __rrshift__ = cache.binary_operator(NDArrayOperatorsMixin.__rrshift__)
    __irshift__ = cache.binary_operator(NDArrayOperatorsMixin.__irshift__)

    __and__ = cache.binary_operator(NDArrayOperatorsMixin.__and__)
    __rand__ = cache.binary_operator(NDArrayOperatorsMixin.__rand__)
    __iand__ = cache.binary_operator(NDArrayOperatorsMixin.__iand__)

    __xor__ = cache.binary_operator(NDArrayOperatorsMixin.__xor__)
    __rxor__ = cache.binary_operator(NDArrayOperatorsMixin.__rxor__)
    __ixor__ = cache.binary_operator(NDArrayOperatorsMixin.__ixor__)

    __or__ = cache.binary_operator(NDArrayOperatorsMixin.__or__)
    __ror__ = cache.binary_operator(NDArrayOperatorsMixin.__ror__)
    __ior__ = cache.binary_operator(NDArrayOperatorsMixin.__ior__)

    __neg__ = cache.unary_operator(NDArrayOperatorsMixin.__neg__)
    __pos__ = cache.unary_operator(NDArrayOperatorsMixin.__pos__)
    __abs__ = cache.unary_operator(NDArrayOperatorsMixin.__abs__)
    __invert__ = cache.unary_operator(NDArrayOperatorsMixin.__invert__)
