class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = s
        stack = deque()

        i = 0
        while i<len(ans):
            if ans[i] == '(':
                stack.append(i)
            
            elif ans[i] == ')':
                l = stack.pop()
                r = i
                rev = ans[l+1:r][::-1]
                ans = ans[:l] + rev + ans[r+1:]

                i = 0
                stack.clear()
                continue
            i += 1
        
        return ans