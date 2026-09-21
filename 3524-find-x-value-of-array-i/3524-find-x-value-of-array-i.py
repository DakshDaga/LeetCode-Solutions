class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        result = [0] * k
        prevCount = [0] * k

        for i in range(n):
            currCount = [0] * k

            currElemRemainder = nums[i] % k
            currCount[currElemRemainder] += 1
            for oldRem in range(k):
                newRem = (oldRem * nums[i] % k) % k
                currCount[newRem] += prevCount[oldRem]

            prevCount, currCount = currCount, prevCount

            for x in range(k):
                result[x] += prevCount[x]

        return result  