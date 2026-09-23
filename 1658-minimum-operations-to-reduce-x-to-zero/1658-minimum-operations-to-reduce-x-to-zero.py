class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        k = sum(nums) - x
        if k < 0: return -1

        left = 0
        tot = 0
        best = -1

        for right, num in enumerate(nums):
            tot += num
            
            while tot > k:
                tot -= nums[left]
                left += 1
            
            if tot == k:
                best = max(best, right - left + 1)
            
        return len(nums)-best if best >= 0 else -1

        