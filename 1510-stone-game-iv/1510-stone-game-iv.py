class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = [-1] * (n+1)
        def helper(n):
            if(n <= 0): return 0
            if memo[n] != -1: return memo[n]
            i = 1
            while i*i <= n:
                if(helper(n - i*i) == 0): 
                    memo[n] = 1
                    return memo[n]
                i += 1
            memo[n] = 0
            return memo[n]
        
        return True if helper(n) == 1 else False