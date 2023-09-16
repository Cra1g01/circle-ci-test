from typing import TypeVar


T = TypeVar("T", int, float)
def add(a: T, b: T) -> T:
    return a + b
