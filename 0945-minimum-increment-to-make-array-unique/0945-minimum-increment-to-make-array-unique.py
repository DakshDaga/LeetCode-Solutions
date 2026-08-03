class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        inc = 0
        for i in range(1, len(nums)):
            if (nums[i] <= nums[i-1]):
                required = nums[i-1] + 1
                inc += required - nums[i]
                nums[i] = required
        return inc