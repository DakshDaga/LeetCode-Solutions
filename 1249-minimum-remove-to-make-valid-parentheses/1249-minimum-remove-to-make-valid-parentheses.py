class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        count = 0
        res = []
        for ch in s:
            if ch == '(':
                res.append(ch)
                count += 1
            elif ch == ')':
                if count <= 0:
                    continue
                res.append(ch)
                count -= 1
            else:
                res.append(ch)
        
        ans = []
        for ch in reversed(res):
            if ch == '(' and count > 0:
                count -= 1
                continue
            ans.append(ch)
        
        return "".join(ans)[::-1]