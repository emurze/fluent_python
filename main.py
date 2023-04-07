import math
from array import array
from collections.abc import Iterator


class Vector2d(object):
    __match_args__ = ('x', 'y')
    typecode = 'd'

    def __init__(self, x, y) -> None:
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self) -> Iterator:
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        return '{}({!r}, {!r})'.format(self.__class__.__name__, *self)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self) -> bytes:
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.x, self.y)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(a, fmt_spec) for a in coords)
        return outer_fmt.format(*components)

    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets[0])
        mem_view = memoryview(octets[1:]).cast(typecode)
        return cls(*mem_view)

    def __hash__(self):
        return hash((self.x, self.y))

    def __complex__(self) -> complex:
        return sum(complex(a) for a in self)

    def __int__(self) -> int:
        return sum(int(a) for a in self)

    def __float__(self) -> float:
        return sum(float(a) for a in self)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    # print(v1.x, v1.y)
    #
    # x, y = v1
    # print(x, y)
    # Vector2d(3.0, 4.0)
    # v1_clone = eval(repr(v1))
    # print(v1 == v1_clone)
    # print(v1)
    #
    # octets = bytes(v1)
    # print(octets)
    # print(abs(v1))
    # print(bool(v1), bool(Vector2d(0, 0)))
    #
    # v1_clone = Vector2d.from_bytes(bytes(v1))
    # print(v1_clone)
    # print(format(v1))
    # print(format(v1, '.2f'))
    # print(format(v1, '.3e'))
    # print(Vector2d(0, 0).angle())
    # print(Vector2d(1, 0).angle())
    #
    # epsilon = 10**-8
    # print((abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon))
    # print(abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon)
    # print(format(Vector2d(1, 1), 'p'))
    # print(format(Vector2d(1, 1), '.3ep'))
    # print(format(Vector2d(1, 1), '0.5fp'))
    #
    # print(v1.x, v1.y)
    # v1 = Vector2d(3, 4)
    # v2 = Vector2d(3.1, 4.2)
    # len({v1, v2})
