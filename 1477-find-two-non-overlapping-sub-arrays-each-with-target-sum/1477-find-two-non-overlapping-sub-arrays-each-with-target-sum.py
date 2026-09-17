class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        i, j = 0, 0
        currSum = 0
        minBestLenTillIdx = [1e9] * n
        minBestLen = 1e9
        result = 1e9

        while(j<n):
            currSum += arr[j]

            while(currSum > target):
                currSum -= arr[i]
                i += 1
            
            if currSum == target:
                l = j - i + 1

                if(i>0 and minBestLenTillIdx[i-1] != 1e9):
                    result = min(result, l + minBestLenTillIdx[i-1])
                
                minBestLen = min(minBestLen, l)
            
            minBestLenTillIdx[j] = minBestLen
            j += 1
        
        return result if result != 1e9 else -1
