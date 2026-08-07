class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        def freeSlotsFiller(n, l):
            filled = ""

            for i in range(9, 1, -1):
                while(n % i == 0):
                    filled += str(i)
                    n //= i
            
            while(len(filled) < l):
                filled += '1'
            
            return filled[::-1]

        n = len(num)
        temp = t
        for primeFact in {2,3,5,7}:
            while(temp % primeFact == 0): temp //= primeFact
        
        if(temp != 1): return '-1'

        remainingFactor = [t] * (n+1)
        for i in range(n):
            digit = int(num[i])
            if(digit == 0): break

            remainingFactor[i+1] = remainingFactor[i] // gcd(remainingFactor[i], digit)
        
        if(remainingFactor[n] == 1): return num

        zeroPos = num.find('0')
        zeroIdx = n-1
        if(zeroPos != -1): zeroIdx = zeroPos

        for i in range(zeroIdx, -1, -1):
            req = remainingFactor[i]
            freeSlots = n-i-1

            for digit in range(int(num[i]) + 1, 10):
                furtherRequired = req // gcd(req, digit)
                requiredNum = freeSlotsFiller(furtherRequired, freeSlots)

                if(len(requiredNum) == freeSlots):
                    return num[0:i] + str(digit) + requiredNum
        
        return freeSlotsFiller(t, n+1)