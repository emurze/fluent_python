from collections import abc


class FrenchDesk(abc.MutableSequence):
    def __init__(self, iterable):
        self._cards = list(iterable)

    def __iter__(self):
        return iter(self._cards)

    def __str__(self):
        return str(tuple(self._cards))

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = self.__class__
            return cls(self._cards[key])
        return self._cards[key]

    def __setitem__(self, key, val):
        self._cards[key] = val

    def __len__(self):
        return len(self._cards)

    def __delitem__(self, key):
        raise NotImplementedError

    def insert(self, index: int, value) -> None:
        self._cards.insert(index, value)


if __name__ == '__main__':
    desk = FrenchDesk([1, 2, 3])
    desk.append(98)
    print(desk)
