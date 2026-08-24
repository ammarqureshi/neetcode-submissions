'''
5,7,3


push 5: diff = 5-5=0, stack[0], min = 5
push 7: diff = 7-5=2, stack[0,2], difference with current min is greater than 0, so keep current min = 5
push 3: diff = 3-5 = -2, stack[0,2,-2] diff smaller than current min, new min = 3

'''


class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0) 
            self.min = val
        
        else: 
          # diff = val - prevMin
            diff = val - self.min
            self.stack.append(diff)

            if diff < 0: 
                self.min = val


    def pop(self) -> None:

        # diff = val - prevMin
        # prevMin = val - diff
        # prevMin = currentMin - diff

        diff = self.stack.pop()
        if diff < 0: 
            # Pop a negative difference:this value created the current minimum, restore the old minimum. 
            self.min = self.min - diff
        
        if not self.stack: 
            self.min = float("inf")

    def top(self) -> int:
        
        diff = self.stack[-1]

        if diff < 0: 
            return self.min
        else: 
            return diff + self.min

    def getMin(self) -> int:
        return self.min
