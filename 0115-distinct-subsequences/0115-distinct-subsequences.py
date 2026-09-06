class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
            
        memo = {}
        def solve(i, j):
            if(j == len(t)): return 1
            if(i == len(s)): return 0

            if (i, j) in memo: return memo[(i, j)]
            if(s[i] == t[j]):
                memo[(i, j)] = solve(i+1, j+1) + solve(i+1, j)

            else: memo[(i, j)] = solve(i+1, j)
            return memo[(i, j)]
        
        return solve(0, 0)