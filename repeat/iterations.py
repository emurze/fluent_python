import re
import reprlib
from collections import abc
from collections.abc import Iterable
from typing import Iterator

RE_WORDS = re.compile(r'\w+')


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text
        self._words = RE_WORDS.findall(text)

    def __iter__(self) -> Iterator:
        return SentenceIterator(self._words)

    def __repr__(self) -> str:
        return f'{type(self).__name__}({reprlib.repr(self.text)})'


def main() -> None:
    sentence = Sentence("lorem1 lorem2 lorem3")
    print(list(iter(sentence)))


def test() -> None:
    print(issubclass(Sentence, Iterable))
    print(issubclass(Sentence, Iterator))

    print(issubclass(SentenceIterator, Iterable))
    print(issubclass(SentenceIterator, Iterator))


if __name__ == '__main__':
    test()

