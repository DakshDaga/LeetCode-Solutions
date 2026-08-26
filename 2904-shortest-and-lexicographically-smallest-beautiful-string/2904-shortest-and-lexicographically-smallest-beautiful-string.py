class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i, j = 0, 0
        n = len(s)
        count = 0
        possibles = []
        while(j<n):
            if s[j] == '1': count += 1
            while(count == k):
                possibles.append(s[i:j+1])
                if(s[i] == '1'): count -= 1
                i += 1
            j += 1
        
        possibles.sort(key=lambda x: (len(x), x))

        return possibles[0] if possibles else ""