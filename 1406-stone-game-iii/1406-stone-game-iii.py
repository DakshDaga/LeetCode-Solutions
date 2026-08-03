class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        n = len(stoneValue)

        def helper(start):
            if(start >= n): return 0
            if start in memo: return memo[start]

            taken = 0
            best = float('-inf')

            for i in range(start, min(start+3, n)):
                taken += stoneValue[i]
                best = max(best, taken - helper(i+1))

            memo[start] = best
            return memo[start]
        
        score = helper(0)
        if score > 0: return "Alice"
        elif score < 0: return "Bob"
        return "Tie"