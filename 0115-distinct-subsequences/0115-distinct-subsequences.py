class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[-1 for _ in range(1001)] for _ in range(1001)]
        def solve(s, t, i, j):
            if(j == len(t)): return 1
            if(i == len(s)): return 0

            if memo[i][j] != -1: return memo[i][j]
            if(s[i] == t[j]):
                memo[i][j] = solve(s, t, i+1, j+1) + solve(s, t, i+1, j)

            else: memo[i][j] = solve(s, t, i+1, j)
            return memo[i][j]
        
        return solve(s, t, 0, 0)