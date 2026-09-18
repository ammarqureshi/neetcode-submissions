class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                # mid is on the high ramp.
                # The minimum must be after mid.
                l = mid + 1
            else:
                # mid could be the minimum.
                r = mid

        return nums[l]