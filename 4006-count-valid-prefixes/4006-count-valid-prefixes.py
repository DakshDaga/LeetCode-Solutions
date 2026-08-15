class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count_1, count_0 = 0, 0
        ans = 0
        for num in s:
            if num == '0': count_0 += 1
            else: count_1 += 1
            if count_0 == count_1 + 1 or count_1 == count_0 + 1 or count_0 == count_1: ans+=1 
        
        return ans