class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 3: return s

        l = list(s)
        mid = ""
        if(n%2 != 0): mid = l.pop(n//2)
        
        l = l[:(n//2)]
        l.sort()
        left = "".join(l)
        return left + mid + left[::-1]