from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Node(Generic[T]):
    """A node in a singly linked list."""
    def __init__(self, data: T, next_node: Optional['Node[T]'] = None):
        self.data = data
        self.next = next_node

class StackLinkedList(Generic[T]):
    """A stack implementation using a singly linked list."""
    def __init__(self) -> None:
        self._top: Optional[Node[T]] = None
        self._size: int = 0

    def push(self, item: T) -> None:
        """Adds an item to the top of the stack."""
        new_node = Node(item, self._top)
        self._top = new_node
        self._size += 1

    def pop(self) -> T:
        """Removes and returns the item at the top of the stack."""
        if self.is_empty() or self._top is None:
            raise IndexError("pop from an empty stack")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self) -> T:
        """Returns the item at the top of the stack without removing it."""
        if self.is_empty() or self._top is None:
            raise IndexError("peek on an empty stack")
        return self._top.data

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return self._top is None

    def size(self) -> int:
        """Returns the number of items in the stack."""
        return self._size
