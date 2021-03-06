from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop
T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    
    return False

C = TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    
    def __eq__(self, other: Any):
        ...
        
    def __it__(self: C, other: C):
        ...
    
    def __gt__(self:C, other:C):
        return (not self < other) and self != other
    
    def __le__(self:C, other:C) -> bool:
        return self < other or self == other

    def __get__(self: C, other: C) -> bool:
        return not self < other
    
    
 