# from collections.abc import Generator
#
#
# def tree(cls, level=0):
#     yield cls, level
#     for c in cls.__subclasses__():
#         yield from tree(c, level+1)
#
#
# def display(cls) -> Generator:
#     for sub_class, level in tree(cls):
#         indent = level * '\t'
#         print(f"{indent}{sub_class.__name__}")
import functools
import itertools
from collections.abc import Iterator
from operator import add, mul
from typing import TypeAlias

if __name__ == '__main__':

    # IntIter: TypeAlias = Iterator[int | str]
    #
    # def fibonacci() -> IntIter:
    #     a, b = 0, 1
    #     while True:
    #         yield a
    #         a, b = b, b + a
    #         if a > 10:
    #             return "Vlad fryed LErka"
    #
    # it = fibonacci()
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # print(next(it))
    # try:
    #     print(next(it))
    # except StopIteration as exp:
    #     print(exp.value)

    money_additions = (10_000, 1.1, 1.05, 1.5, 0.67, 0.43,
                       0.1, 1.4, 2.6, 5.8, 58.8, 683.6)

    def refactor(obj: float):
        if obj == 0:
            return "000"
        if obj < 10:
            return round(obj * 100)
        if obj < 100:
            return round(obj * 10)
        return round(obj)

    def transform_money(money: float):
        ext: str = ''
        while money >= 1000:
            money, res = divmod(money, 1000)
            ext += f'_{refactor(res)}'
        return f"{int(money)}{ext}"

    print(*map(lambda i: f"{transform_money(i)}$",
               itertools.accumulate(money_additions, mul)))

