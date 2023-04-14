# import inspect
# from abc import abstractmethod
# from collections import namedtuple
from dataclasses import dataclass, field, InitVar
from typing import runtime_checkable, Protocol
# from typing import NamedTuple, ClassVar  # ClassVar

# l1 = namedtuple('Coords', 'lat lot', defaults=(1,))
# print(l1(1)._fields)


# class Coords(NamedTuple):
#     lat: float
#     lot: float
#     ref: str = 'https://lerka.vlad'
#     history: list = []
#
#
# coords = Coords(1, 2)
# coords.history.extend([1, 2])
# print(Coords(2, 4))
# print(coords[0])
# print(inspect.get_annotations(Coords))
# print(frozenset([2, 3, 3]))


@dataclass(frozen=True, eq=True, order=True)
class Coords:
    lat: float
    lot: float
    _history: list[str] = field(default_factory=list, kw_only=True)
    secret: InitVar[str | None] = field(default=None, kw_only=True)

    def __post_init__(self, secret):
        self._history.append(secret)


coords = Coords(1, 2, secret="HE HE")


@runtime_checkable
class SupportLt(Protocol):
    def close(self): pass


class TestObj:
    def __init__(self):
        pass


obj = 1
print(isinstance(TestObj(), SupportLt))
