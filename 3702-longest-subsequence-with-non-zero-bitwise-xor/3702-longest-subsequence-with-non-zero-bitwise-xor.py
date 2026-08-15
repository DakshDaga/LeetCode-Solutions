class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == [0]*n: return 0
        curr = 0
        for num in nums: 
            curr ^= num
        
        return n if curr else n-1

        