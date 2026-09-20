class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s):
            idx = 26 - (ord(ch) - 97)
            ans += idx * (i+1)
        
        return ans