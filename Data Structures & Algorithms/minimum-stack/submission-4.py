'''
5,7,3


push 5: diff = 5-5=0, stack[0], min = 5
push 7: diff = 7-5=2, stack[0,2], difference with current min is greater than 0, so keep current min = 5
push 3: diff = 3-5 = -2, stack[0,2,-2] diff smaller than current min, new min = 3

'''


class MinStack:

    def __init__(self):
        # This stack stores encoded differences, not the original values.
        self.stack = []
        # The current minimum lets us decode the top value in O(1).
        self.min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            # The first value is the minimum. Its difference from itself is 0.
            self.stack.append(0)
            self.min = val
            return

        # Calculate the difference using the OLD minimum before updating it.
        difference = val - self.min
        self.stack.append(difference)

        # A negative difference means val is smaller than the old minimum.
        # It is now the new minimum.
        if difference < 0:
            self.min = val

    def pop(self) -> None:
        # The problem guarantees pop is called only when the stack has items.
        difference = self.stack.pop()

        # A negative difference means the popped value created the current min.
        # Reverse: difference = popped_value - previous_minimum.
        # Since popped_value is current min, previous_minimum = min - difference.
        if difference < 0:
            self.min = self.min - difference

        # This reset is only for a clean state if every item was removed.
        if not self.stack:
            self.min = float("inf")

    def top(self) -> int:
        difference = self.stack[-1]

        # Non-negative: actual value = difference + current minimum.
        if difference >= 0:
            return difference + self.min

        # Negative: this value created the current minimum, so it equals min.
        return self.min

    def getMin(self) -> int:
        # The current minimum is stored separately, so this is O(1).
        return self.min