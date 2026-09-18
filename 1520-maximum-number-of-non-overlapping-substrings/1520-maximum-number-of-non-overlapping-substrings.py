class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        start = [-1] * 26
        end = [-1] * 26
        isValid = [True] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if start[idx] == -1:
                start[idx] = i
            
            end[idx] = i

        for ch in range(26):
            if start[ch] == -1: continue

            i = start[ch]
            while i < end[ch]:
                idx = ord(s[i]) - ord('a')
                if start[idx] < start[ch]:
                    isValid[ch] = False
                    break
                
                end[ch] = max(end[ch], end[idx])
                i += 1
        
        result = []
        lastTakenStart = 1e9
        for i in range(n-1, -1, -1):
            ch_idx = ord(s[i]) - ord('a')
            if not isValid[ch_idx]: continue

            if i == start[ch_idx] and lastTakenStart > end[ch_idx]:
                result.append(s[i : end[ch_idx]+1])
                lastTakenStart = i

        return result