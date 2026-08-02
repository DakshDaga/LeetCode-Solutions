class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def helper(left, right):
            if(left == right): return piles[left]
            if (left, right) in memo: return memo[(left, right)]

            take_left = piles[left] - helper(left+1, right)
            take_right = piles[right] - helper(left, right-1)

            memo[(left, right)] = max(take_left, take_right)
            return memo[(left, right)]
        
        return helper(0, len(piles)-1) > 0