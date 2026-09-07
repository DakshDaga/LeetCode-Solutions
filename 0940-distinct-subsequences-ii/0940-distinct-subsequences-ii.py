class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [-1] * 2001

        def solve(n):
            if(n == 0):
                return 1
            
            if dp[n] != -1: return dp[n]

            ans = (2 * solve(n-1)) % MOD
            if prev[n] != 0:
                duplicates = solve(prev[n] - 1)
                ans = (ans - duplicates) % MOD

            dp[n] = ans
            return dp[n]
        
        lastSeen = [0] * 26
        prev = [0] * (len(s)+1)
        for i in range(1, len(s)+1):
            ch = ord(s[i-1]) - ord('a')
            prev[i] = lastSeen[ch]
            lastSeen[ch] = i
        
        return (solve(len(s)) - 1 + MOD) % MOD