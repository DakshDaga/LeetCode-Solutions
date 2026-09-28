class Solution:
    def maxDepth(self, s: str) -> int:
        count, ans = 0, 0
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
            ans = max(count, ans)
        
        return ans