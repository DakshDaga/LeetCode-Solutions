class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxLen = 0
        counts = {}
        i = 0
        for j, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            while(counts[ch] > 2):
                counts[s[i]] -= 1
                i += 1
            maxLen = max(maxLen, j-i+1)
        
        return maxLen