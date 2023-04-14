# from functools import lru_cache
# from operator import attrgetter
# from random import random
# from typing import TypeVar
#
# from devtools.checking import checking
# from collections import Counter, ChainMap
#
# l1 = [f"{random()*9:.0f}" for _ in range(10_000)]
# print(len(l1))
#
#
# def remove_all(_list: list, elem) -> None:
#     while True:
#         try:
#             _list.remove(elem)
#         except ValueError:
#             break
#
#
# remove_all(l1, elem='1')
# print(len(l1))
#
# string = ''.join(l1)
#
#
# @lru_cache(maxsize=16)
# @checking
# def counter(_string: str, /) -> dict:
#     _count = {}
#     for st in _string:
#         if _count.get(st):
#             _count.setdefault(st, _string.count(st))
#     return _count
#
#
# T = TypeVar("T")
#
#
# @lru_cache(maxsize=16)
# @checking
# def counter2(_string: T, /) -> list[tuple[T, int]]:
#     _count = Counter(_string)
#     return _count.most_common(3)
#
#
# for count in counter(string).items():
#     print('%s | %s' % count)
# print(sum(counter(string).values()))
#
# for count in counter2(string):
#     print('%s | %s' % count)
# print(sum(x[1] for x in counter2(string)))


# def all_index(_list: list, elem) -> set[int]:
#     _all_idx = set()
#     cnt = 0
#     try:
#         while idx := _list.index(elem):
#             _list.pop(idx)
#             _all_idx.add(cnt := cnt+1)
#     except ValueError:
#         return _all_idx
#
#
# print(all_index(l1, '3'))


# print(l1.extend(map(str, [1, 2, 3, 4])))
# print(l1)


# d1 = dict.fromkeys(l1, 'LERKA')
# print('1' in d1)

# s1 = set(int(f"{random()*100:.0f}") for _ in range(100))
# s1 |= {100}
# print(s1 - {100})
# print(s1.pop())

# d1 = {"a": 1, "b": 2, "c": 3}
# print(d1.keys() & {"c"})

# match l1:
#     case (object(), b as trash, *_) if trash:
#         print(len(trash))
