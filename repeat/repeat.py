# import json
# import dataclasses
from _decimal import Decimal
from collections.abc import Iterator
from dataclasses import dataclass, field
from enum import Enum, auto
from operator import attrgetter
from typing import Generic, TypeVar, Protocol


class Request(Enum):
    OK = auto()
    BAD = auto()


class UserException(Exception):
    def __init__(self, value: str = ''):
        self.value = value

    def __str__(self):
        msg = self.__class__.__doc__ or ''
        if self.value:
            msg.rstrip(".")
            if "'" in self.value:
                value = self.value
            else:
                value = repr(self.value)
            msg += f": {value}"
        return msg


class MoneyValidationError(UserException):
    """Money must be >= 0."""


@dataclass(eq=True, frozen=True, order=True)
class User:
    name: str
    password: str = field(repr=False)
    money: Decimal = 0

    def __post_init__(self):
        if self.money < 0:
            raise MoneyValidationError()


K = TypeVar("K")
T = TypeVar("T")


class IterableSized(Protocol[K]):
    def __iter__(self) -> Iterator[K]: ...
    def __len__(self) -> int: ...


class Server(Generic[T]):
    def __init__(self, _items: IterableSized[T] | None = None, /) -> None:
        self._items = _items

    @staticmethod
    def accept(request: Request):
        if request.OK == Request.OK:
            print("Good connection.")
        else:
            print("Bad connection.")

    def __add__(self, other):
        if ...:
            return NotImplemented

    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        items_msg = ', '.join(repr(item) for item in self._items)
        if len(self._items) > 1:
            return f"{cls_name}: [{items_msg}]"
        return f"{cls_name}: {items_msg}"


class Saver:
    def __enter__(self, *args): ...
    def __exit__(self, *args): ...


TL = TypeVar("TL", int, str)


def test(a, b, c):
    if (all(isinstance(i, int) for i in (a, b, c)) or
            all(isinstance(i, str) for i in (a, b, c))):
        return a+b+c
    return None


if __name__ == '__main__':
    user1 = User("Vlad", "qwerty", Decimal(1))
    user2 = User("Vlad2", "qwerty", Decimal(53))
    user3 = User("Vlad3", "qwerty", Decimal(32))
    sorted_users = sorted([user1, user2, user3], key=attrgetter('money'))
    server = Server(sorted_users)
    print(server)

    # with open('product.json', 'r') as f:
    #     product = json.load(f)
    # print(product)
    #
    # with Saver():
    #     server.accept(Request.BAD)
    #
    # print(str(user3).ljust(40) + "VLAD")

    # ge = dataclasses.asdict(user1).keys()
    # print(ge - {'money'})
