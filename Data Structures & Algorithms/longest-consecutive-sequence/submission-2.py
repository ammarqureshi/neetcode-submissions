class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet: 
            if (num - 1) not in numSet: 
                #starting sequence
                currentLen = 1
                while(num + currentLen) in numSet: 
                    currentLen += 1
                longest = max(longest, currentLen)
        return longest