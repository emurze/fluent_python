import functools
import math
import reprlib
from array import array
from collections.abc import Iterable
from operator import xor
from random import random


class Vector:
    __match_args__ = ("x", "y", "c", "d")
    typecode = 'd'

    def __init__(self, iterable: Iterable):
        self._components = list(iterable)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = self.__class__
            return cls(self._components[key])
        return self._components[key]

    def __getattr__(self, item):
        try:
            pos = self.__match_args__.index(item)
        except ValueError:
            pos = -1
        if 0 <= pos <= len(self.__match_args__)-1:
            return self._components[pos]
        raise ValueError(f"Attribute {item} doesn't exist")

    def __setattr__(self, key, value):
        if len(key) == 1:
            cls_name = self.__class__.__name__
            if key in self.__match_args__:
                err = 'Key {attr_name!r} in immutable tuple.'
            elif key.islower():
                print(1)
                err = "Cannot set attribute 'a' to 'z' in {cls_name!r}"
            else:
                err = ""
            if err:
                raise AttributeError(err.format(attr_name=key,
                                                cls_name=cls_name))
        super().__setattr__(key, value)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        repr_view = reprlib.repr(self._components)
        components = repr_view[repr_view.find('[')+1:-1]
        print(components)
        return f"{self.__class__.__name__}({components})"

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(xor, hashes, 0)

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

    def __bytes__(self) -> bytes:
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets[0])
        mem_view = memoryview(octets[1:]).cast(typecode)
        return cls(*mem_view)


if __name__ == '__main__':
    vector1 = Vector(set(round(random()*100) for _ in range(100)))
    print(vector1[4])
