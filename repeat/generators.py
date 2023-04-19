from functools import reduce
from itertools import takewhile, cycle, count, pairwise, starmap, chain, \
    groupby, tee, accumulate
import random
import re
import reprlib
from collections.abc import Generator, Iterator
from operator import mul, add

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text

    def __iter__(self) -> Generator:
        return (x.group() for x in RE_WORD.finditer(self.text))

    def __repr__(self) -> str:
        return f'{type(self).__name__}({reprlib.repr(self.text)})'


class ArifProg:
    def __init__(self, begin: float, step: float, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self) -> Iterator:
        first = type(self.begin + self.step)(self.begin)
        _ap_gen = count(first, self.step)
        if self.end is None:
            return _ap_gen
        return takewhile(lambda x: x < self.end, _ap_gen)


if __name__ == '__main__':
    # sentence = Sentence("lorem1 lorem2 lorem3")
    # for i in sentence:
    #     print(i)

    # ap = ArifProg(1, .5, 5)
    # print(list(ap))

    r_range = (random.randrange(50_000) for _ in range(800))
    print(help(pairwise))
