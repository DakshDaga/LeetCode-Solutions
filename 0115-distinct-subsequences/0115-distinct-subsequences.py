class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0
            
        memo = {}
        def solve(i, j):
            if i == m or j == n or m - i < n - j:
                return int(j == n)

            if (i, j) in memo: return memo[(i, j)]
            if(s[i] == t[j]):
                memo[(i, j)] = solve(i+1, j+1) + solve(i+1, j)

            else: memo[(i, j)] = solve(i+1, j)
            return memo[(i, j)]
        
        return solve(0, 0)