class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pref_max = nums[0]
        sumOfPref = pref_max
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                pref_max = nums[i]
                sumOfPref += pref_max
            else: break
        
        while(sumOfPref in nums):
            sumOfPref += 1
        return sumOfPref
