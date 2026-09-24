class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digits = [int(x) for x in str(num)]
            if sum(digits) == i:
                return i
        
        return -1