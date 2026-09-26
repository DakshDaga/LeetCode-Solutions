class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = dict(knowledge)
        ans = ""
        i = 0
        while i < len(s): 
            if s[i] == '(':
                key = ""
                i += 1
                while s[i] != ')':
                    key += s[i]
                    i += 1          
                ans += mp.get(key, "?")

            else:
                ans += s[i]
            i += 1

        return ans
            
