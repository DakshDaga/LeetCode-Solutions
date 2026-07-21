class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        temp = []

        for ch in s:
            freq[ch] -= 1
            if ch in seen: continue

            while temp and temp[-1] > ch and freq[temp[-1]] > 0:
                seen.remove(temp.pop())
            
            seen.add(ch)
            temp.append(ch)

        ans = "".join(temp)
        return ans