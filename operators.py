import itertools
from abc import abstractmethod
from collections import abc
from collections.abc import Iterable, Iterator
from typing import TypeVar, Generic, Protocol

from fluent_python.realize_abc import BingoCase

T = TypeVar("T")


class SupportsIterableAndLen(Protocol):
    @abstractmethod
    def __len__(self) -> int: ...
    @abstractmethod
    def __iter__(self) -> Iterator: ...


class Vector(Generic[T]):
    def __init__(self, iterable: Iterable[T]) -> None:
        self._items: tuple[T] = tuple(iterable)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return (item for item in self._items)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a+b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f"{type(self).__name__}{tuple(self)}"

    def __mul__(self, scalar):
        try:
            float(scalar)
        except TypeError:
            return NotImplemented
        return Vector(item * scalar for item in self._items)

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other: SupportsIterableAndLen):
        if all(isinstance(other, x) for x in (abc.Iterable, abc.Sized)):
            return sum(a * b for a, b in
                       zip(self, other, strict=True))
        return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) and
                    all(a == b for a, b in zip(self, other)))
        return NotImplemented


class AddableBingoCase(BingoCase):
    def __add__(self, other):
        if isinstance(other, cls := type(self)):
            return cls(self.inspect() + other.inspect())
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            _other_iter = other.inspect()
        else:
            try:
                _other_iter = iter(other)
            except TypeError:
                raise ValueError("HE HE")
        self.load(_other_iter)
        return self


if __name__ == '__main__':
    a3 = AddableBingoCase([4])
    a3 += [3]
    # print(a3)

    vector = Vector([1, 2, 3])

    vector @ 3
