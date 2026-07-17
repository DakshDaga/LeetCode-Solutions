class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxVal = max(nums)

        freq = [0] * (maxVal + 1)
        for x in nums:
            freq[x] += 1

        divCnt = [0] * (maxVal + 1)

        for g in range(1, maxVal + 1):
            for x in range(g, maxVal + 1, g):
                divCnt[g] += freq[x]

        exact = [0] * (maxVal + 1)

        for g in range(maxVal, 0, -1):

            exact[g] = divCnt[g] * (divCnt[g] - 1) // 2

            for m in range(2 * g, maxVal + 1, g):
                exact[g] -= exact[m]

        prefix = [0] * (maxVal + 1)

        for g in range(1, maxVal + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        ans = []

        for q in queries:
            g = bisect_left(prefix, q + 1, 1)
            ans.append(g)

        return ans