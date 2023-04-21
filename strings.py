import inspect
import numbers
from collections.abc import Callable, Hashable
from operator import methodcaller

with open("lorem.txt", "r", encoding='utf-8') as f:
    text = f.read()

# print(text := text.swapcase())
# print(text.swapcase())
#
# text = text.split()
#
# upper = methodcaller('upper')
# print(list(map(upper, text)) == list(map(str.upper, text)))

# print(text.translate(None, "a"))
# print(help(str.index))
# print(help(Hashable))
# print(help(set))


class Lera:
    """Fat bunny"""


print(inspect.getmro(numbers.Integral))
