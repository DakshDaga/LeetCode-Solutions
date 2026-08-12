class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        maxWindow = 0
        counts = {}
        for j, num in enumerate(nums):
            counts[num] =  counts.get(num, 0) + 1
            while(counts[num] > k):
                counts[nums[i]] -= 1
                i += 1
            maxWindow = max(maxWindow, j-i+1)
        
        return maxWindow
