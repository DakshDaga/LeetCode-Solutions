class Solution:
    def nCr(self, n: int, r: int, k: int) -> int:
        r = min(r, n-r)
        result = 1
        for i in range(1, r+1):
            result = result * (n-r+i) // i
            if(result >= k): return result
        
        return result

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half = n//2
        mid = ""
        if(n%2 != 0): mid += s[half]

        counts = [0] * 26
        for i in range(n):
            if(n%2 != 0 and i == half): continue
            counts[ord(s[i]) - ord('a')] += 1
        
        counts[:] = [x//2 for x in counts]

        halfResult = ""
        for i in range(half):
            isValid = False
            for j in range(26):
                if(counts[j] ==  0): continue
                counts[j] -= 1

                # Count no. of ways
                ways = 1
                letters = sum(counts)

                for c in counts:
                    if c:
                        ways *= self.nCr(letters, c, k)
                        letters -= c
                    
                    if ways >= k: break
                
                if ways >= k:
                    halfResult += chr(j + ord('a'))
                    isValid = True
                    break

                k -= ways
                counts[j] += 1
            
            if(not isValid): return ""
        
        return halfResult + mid + halfResult[::-1]