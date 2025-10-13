class MinStack:
    """
    A stack that supports push, pop, top, and retrieving the minimum
    element in constant time.
    """
    def __init__(self):
        # Main stack to store elements
        self._stack = []
        # Auxiliary stack to store the minimum element at each stage
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        # If min_stack is empty or the new value is <= the current min, push it
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        if not self._stack:
            return
        
        # If the popped element is the current minimum, pop from min_stack too
        if self._stack.pop() == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> int:
        if not self._stack:
            raise IndexError("top from an empty stack")
        return self._stack[-1]

    def get_min(self) -> int:
        if not self._min_stack:
            raise IndexError("get_min from an empty stack")
        return self._min_stack[-1]
