import abc
import random
from collections.abc import Iterable
from collections import UserList
from typing import NoReturn, Any


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable: Iterable) -> None:
        """Load items from iterable"""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random. Returning it.

        This method should raise LookupError when the instance is empty.
        """

    def loaded(self) -> bool:
        """Return True if there's at least 1 item, False otherwise."""
        return bool(self.inspect())

    def inspect(self) -> tuple:
        """Return a sorted tuple with the items currently inside."""
        items: list = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)


class BingoCase(Tombola):
    def __init__(self, items: Iterable) -> None:
        self._randomizer = random.SystemRandom()
        self._items: list = []
        self.load(items)

    def pick(self) -> Any | NoReturn:
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Pick from empty BingoCase.")

    def load(self, iterable: Iterable) -> None:
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def loaded(self) -> bool:
        return bool(self._items)

    def clear(self) -> None:
        self._items.clear()

    def __repr__(self) -> str:
        return str(self.inspect())


class LottoBlower(Tombola):
    def __init__(self, iterable: Iterable) -> None:
        self._items = list(iterable)

    def pick(self) -> Any | NoReturn:
        try:
            pos = random.randrange(len(self._items))
        except ValueError:
            raise LookupError("LottoBlower is empty.")
        return self._items.pop(pos)

    def load(self, iterable: Iterable) -> None:
        self._items.extend(iterable)

    def loaded(self) -> bool:
        return bool(self._items)

    def inspect(self) -> tuple:
        return tuple(self._items)


@Tombola.register  # type: ignore
class TombolaList(list):
    def pick(self):
        if self:
            pos = random.randrange(len(self))
            return self.pop(pos)
        else:
            raise LookupError("TombolaList is empty.")

    load = UserList.extend

    def loaded(self):
        return bool(self)

    # def inspect(self):
    #     return tuple(self)


if __name__ == '__main__':
    t = TombolaList(range(100))
    print(isinstance(t, Tombola))
    t.inspect()
    print(TombolaList.__mro__)
