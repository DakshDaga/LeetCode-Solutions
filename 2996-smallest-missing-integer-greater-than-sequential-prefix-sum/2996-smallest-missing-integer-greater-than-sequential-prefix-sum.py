class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pref_sum = nums[0]
        idx = 1
        while idx < len(nums) and nums[idx] == nums[idx-1] + 1:
                pref_sum += nums[idx]
                idx += 1
        
        while(pref_sum in nums):
            pref_sum += 1
        return pref_sum
