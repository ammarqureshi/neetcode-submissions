class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        '''
        stack = (start_ix, height)
        ''' 
        stack = [] 

        for i,h in enumerate(heights): 
            start_ix = i
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start_ix = index
            stack.append((start_ix,h))
        


        for i,h in stack: 
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea