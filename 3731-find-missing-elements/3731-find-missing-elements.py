class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        curr = nums[0]
        ans = []
        for i in range(len(nums)):
            while(curr != nums[i]):
                ans.append(curr)
                curr += 1
            curr += 1
        return ans
