class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)
        rhsMatchLength = [0] * m

        # Filling rhsMatchLength
        i, j = m-1, n-1
        rightMatched = 0
        while(i>=0):
            if(j>=0 and word1[i] == word2[j]):
                rightMatched += 1
                rhsMatchLength[i] = rightMatched
                i -= 1
                j -= 1
            else:
                rhsMatchLength[i] = rightMatched
                i -= 1
        
        ans = []
        canChange = True
        i = j = 0
        while(i<m and j<n):
            if(word1[i] == word2[j]):
                ans.append(i)
                j += 1
            elif(canChange and i+1 < m and rhsMatchLength[i+1] >= n-j-1):
                ans.append(i)
                j += 1
                canChange = False
            i += 1
        
        return ans if len(ans) == n else []
                
