class Solution:
    def countValidPrefixes(self, s: str) -> int:
        counts = [0] * 2
        ans = 0
        for num in s:
            if num == '0': counts[0] += 1
            else: counts[1] += 1
            if abs(counts[0] - counts[1]) <= 1: ans+=1 
        
        return ans