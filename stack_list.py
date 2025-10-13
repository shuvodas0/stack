from typing import Generic, TypeVar, List

T = TypeVar('T')

class Stack(Generic[T]):
    """
    A stack implementation that uses a Python list as the underlying data store.
    """
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Adds an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Removes and returns the item at the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Returns the item at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek on an empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return not self._items

    def size(self) -> int:
        """Returns the number of items in the stack."""
        return len(self._items)

    def __str__(self) -> str:
        return str(self._items)

if __name__ == '__main__':
    # Example Usage
    s = Stack[int]()
    print(f"Is stack empty? {s.is_empty()}")
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Stack: {s}")
    print(f"Stack size: {s.size()}")
    print(f"Peek: {s.peek()}")
    print(f"Popped: {s.pop()}")
    print(f"Stack after pop: {s}")
