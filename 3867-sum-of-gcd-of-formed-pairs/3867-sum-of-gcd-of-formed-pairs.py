class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        maxArray = []
        for i in range(n):
            if i==0:
                maxArray.append(nums[i])
                continue
            maxArray.append(max(nums[i], maxArray[i-1]))
        
        prefixGCD =  []
        for i in range(n):
            prefixGCD.append(gcd(nums[i], maxArray[i]))
        
        prefixGCD.sort()

        sum_of_gcd = 0
        i, j = 0, n-1
        while(i<j):
            sum_of_gcd += gcd(prefixGCD[i], prefixGCD[j])
            i+=1
            j-=1

        return sum_of_gcd