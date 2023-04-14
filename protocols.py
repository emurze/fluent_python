from collections import UserDict
from typing import Protocol, TypeVar, Any

T = TypeVar("T")


class SupportMul(Protocol):
    def __iter__(self: T, repeat_count: int) -> T: ...


RT = TypeVar("RT", bound=SupportMul)


def test(_obj: RT) -> RT:
    return _obj*2


class MyDict(UserDict):
    pass


if __name__ == '__main__':
    def test1(obj: Any) -> None:
        try:
            int(obj)
            float(obj)
            complex(obj)
            hash(obj)
            callable(obj)
            str(obj)
            bool(obj)
            iter(obj)
            tuple(obj)
            list(obj)
            set(obj)
            frozenset(obj)
            dict(obj)
        except ValueError:
            pass

    print(vars(MyDict(a=3, b=5)), dir(MyDict), help(MyDict))
