from collections import UserDict


class Root:
    def ping(self):
        mro.pop(0)
        print(f"method ping in Root")
        print(f"{mro}\n")

    def pong(self):
        print(f"method pong in Root")


class A(Root):
    def ping(self):
        print(f"method ping in A")
        mro.pop(0)
        print(f"{mro}\n")
        super().ping()

    def pong(self):
        print(f"method pong in A")
        super().pong()


class B(Root):
    def ping(self):
        print(f"method ping in B")
        mro.pop(0)
        print(f"{mro}\n")
        super().ping()

    def pong(self):
        print(f"method pong in B")
        super().pong()


class Leaf(B, A):
    def ping(self):
        print(f"method ping in {self.__class__.__name__}")
        mro.pop(0)
        print(f"{mro}\n")
        super().ping()

    def pong(self):
        print(f"method pong in {self.__class__.__name__}")
        super().pong()


if __name__ == '__main__':
    leaf = Leaf()
    mro = list(Leaf.__mro__)
    leaf.ping()
