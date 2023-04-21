from typing import overload


@overload
def test(a: int, b: int, c: int) -> int: ...
@overload
def test(a: str, b: str, c: str) -> str: ...
