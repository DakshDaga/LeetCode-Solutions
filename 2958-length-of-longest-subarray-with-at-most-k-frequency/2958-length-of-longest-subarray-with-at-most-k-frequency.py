class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = 0
        maxSize = 0
        counts = {}
        while(j<n and i<n):
            counts[nums[j]] =  counts.get(nums[j], 0) + 1
            while(counts[nums[j]] > k):
                counts[nums[i]] -= 1
                i += 1
            maxSize = max(maxSize, j-i+1)
            j += 1
        
        return maxSize
