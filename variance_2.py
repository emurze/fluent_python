from abc import abstractmethod
from typing import Protocol, runtime_checkable, TypeVar

ABS = TypeVar("ABS", covariant=True)


@runtime_checkable
class SupportsAbs(Protocol[ABS]):
    @abstractmethod
    def __lt__(self) -> ABS: ...


class Spam:
    ...


class SubSpam(Spam):
    ...


def is_unit(obj: SupportsAbs[float]):
    print(obj)


if __name__ == '__main__':
    print(hasattr(SubSpam, '__lt_'))
    print(isinstance(SubSpam(), SupportsAbs))
