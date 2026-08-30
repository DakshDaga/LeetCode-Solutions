class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxIdx = nums.index(max(nums))
        minIdx = nums.index(min(nums))

        n = len(nums)

        leftDel = max(maxIdx, minIdx) + 1
        rightDel = max(n-maxIdx, n-minIdx)
        alternate = maxIdx+1 + n-minIdx if maxIdx < minIdx else minIdx+1 + n-maxIdx

        return min(leftDel, rightDel, alternate)