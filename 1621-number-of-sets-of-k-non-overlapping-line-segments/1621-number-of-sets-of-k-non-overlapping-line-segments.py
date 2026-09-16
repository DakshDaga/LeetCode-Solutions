class Solution:
    def numberOfSets(self, n: int, K: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        MOD = 10**9 + 7
        
        for i in range(n):
            dp[0][i] = 1
        
        for k in range(1, K+1):
            prevRowSum = [0] * (n+1)
            for x in range(n-1, -1, -1):
                prevRowSum[x] = (prevRowSum[x+1] + dp[k-1][x]) % MOD

            for i in range(n-1, -1, -1):
                skip = dp[k][i+1] % MOD
                take = prevRowSum[i+1]
                dp[k][i] = skip + take
        
        return dp[K][0] % MOD