class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        unique = set(nums)
        i = 1
        while True:
            if k*i not in unique: return k*i
            else: i += 1