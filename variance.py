from collections.abc import Iterable
from typing import TypeVar, Generic


class Beverage:
    ...


class Juice(Beverage):
    ...


class OrangeJuice(Juice):
    ...


T = TypeVar("T")


class BeverageDispenser(Generic[T]):
    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage

    def install(self, dispenser: 'BeverageDispenser[Juice]') -> None: ...


K = TypeVar("K")


class Queue(Generic[K]):
    def __init__(self, obj: K): ...

    def append(self, item: K): ...

    def pop(self): ...

    def test(self, obj: 'Queue[Juice]'):
        return f"{obj}"


if __name__ == '__main__':
    juice_dispenser = BeverageDispenser(Juice())
    # juice_dispenser.install(juice_dispenser)
    #
    # beverage_dispenser = BeverageDispenser(Beverage())
    # juice_dispenser.install(beverage_dispenser)
    #
    # orange_juice_dispenser = BeverageDispenser(OrangeJuice())
    # juice_dispenser.install(orange_juice_dispenser)

    queue: Queue[Juice] = Queue(Juice())
    queue.test(queue)
