from typing import TypeVar, Generic, cast


class Beverage:
    ...


class Juice(Beverage):
    ...


class OrangeJuice(Juice):
    ...


T = TypeVar("T", contravariant=True)


class BeverageDispenser(Generic[T]):
    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def install(self, dispenser: 'BeverageDispenser[Juice]') -> None: ...


if __name__ == '__main__':
    # juice_dispenser = BeverageDispenser(Juice())
    # juice_dispenser.install(juice_dispenser)
    #
    # beverage_dispenser = BeverageDispenser(Beverage())
    # juice_dispenser.install(beverage_dispenser)
    #
    # orange_juice_dispenser = BeverageDispenser(OrangeJuice())
    # juice_dispenser.install(orange_juice_dispenser)

    l1: list[float] = []
    l2: list[int] = []
    l3 = cast(list[int], l1)
    print(l3 is l2)
