'''
[30,38,30,36,35,40,28]

38,30,

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack keeps increasing
        res = [0] * len(temperatures)
        stack = [] # (temp, ix)


        for i, temp in enumerate(temperatures):

            # keep popping out temperatures from stack that were waiting for a temp greather than them
            while stack and temp > stack[-1][0]: 
                stackTemp, stackIx = stack.pop()
                res[stackIx] = i - stackIx
            stack.append((temp, i))
        return res
 