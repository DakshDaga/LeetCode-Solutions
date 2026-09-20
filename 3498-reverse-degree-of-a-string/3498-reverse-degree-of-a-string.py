class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s):
            idx = abs(ord(ch) - ord('a') - 26)
            ans += idx * (i+1)
        
        return ans