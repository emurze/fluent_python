from _decimal import Decimal
from collections.abc import Container, Sized, Iterable, Collection
from typing import Protocol, TypeVar, SupportsComplex, runtime_checkable


class Test:
    def __contains__(self, item): pass
    def __len__(self): pass
    def __iter__(self): pass


T = TypeVar("T")


class SupportMul(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...


RT = TypeVar("RT", bound=SupportMul)


def test(obj: RT) -> RT:
    return obj*2


@runtime_checkable
class SupportsFloat(Protocol):
    def __float__(self) -> float: ...


if __name__ == '__main__':
    print(isinstance(Decimal(3), SupportsFloat))

