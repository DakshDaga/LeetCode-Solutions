class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxArr, minArr = [-1]*n, [-1]*n
        i, j = 0, n-1
        tempMax, tempMin = -1, 1e9
        while(i<n):
            tempMax = max(tempMax, nums[i])
            tempMin = min(tempMin, nums[j])
            maxArr[i] = tempMax
            minArr[j] = tempMin
            i += 1
            j -= 1
        
        for i in range(n):
            if(maxArr[i] - minArr[i] <= k): return i
        
        return -1