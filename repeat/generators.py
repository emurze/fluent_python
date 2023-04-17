import re
import reprlib
from collections.abc import Generator

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text

    def __iter__(self) -> Generator:
        return (x.group() for x in RE_WORD.finditer(self.text))

    def __repr__(self) -> str:
        return f'{type(self).__name__}({reprlib.repr(self.text)})'


if __name__ == '__main__':
    sentence = Sentence("lorem1 lorem2 lorem3")
    for i in sentence:
        print(i)
