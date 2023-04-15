import random
from _decimal import Decimal
from collections.abc import Iterable
from dataclasses import field, dataclass

from typing import TypeVar, Generic, TypeAlias

from exceptions import RangeListIsEmpty

T = TypeVar("T")


@dataclass(eq=True, frozen=True)
class User:
    first_name: str
    last_name: str
    password: str
    password_hint: str = field(repr=False)
    friends: list[str] = field(default_factory=list)


class Registry:
    def __init__(self, user: T | None = None) -> None:
        self._users: list[T] = [user] if user else []
        print(type(user))

    def register(self, user: T) -> T:
        self._users.append(user)
        print(type(user))
        return user

    def get_users(self) -> list[T]:
        return self._users


RANGE = TypeVar("RANGE")
ITER_RANGE: TypeAlias = Iterable[RANGE]


class Range(Generic[RANGE]):
    """Custom range ... ."""

    def __init__(self, items: ITER_RANGE) -> None:
        self._list = list(items) if items else []

    def put(self, item: RANGE) -> None:
        self._list.append(item)

    def take_away(self, elem=None) -> RANGE:
        if not self._list:
            raise RangeListIsEmpty("Range is empty.")
        if elem:
            return self._list.remove(elem)
        random_idx = random.randrange(len(self._list))
        return self._list.pop(random_idx)

    def __len__(self):
        return len(self._list)

    def __repr__(self):
        cls = self.__class__
        return f"{cls.__name__}({', '.join(map(str, self._list))})"


if __name__ == '__main__':
    # user1 = User('Vlad', 'Zama_tev_ski', "qwerty", "Lera")
    # user2 = User('Vlad2', 'Zama_tev_ski2', "qwerty2", "Lera2")
    #
    # registry = Registry(user1)
    # registry.register(user2)
    # print(registry.get_users())

    r_range = Range[Decimal](Decimal(f'{num:.1f}') for num in range(20))
    while r_range:
        print(r_range.take_away())
    else:
        print("good luck!")
