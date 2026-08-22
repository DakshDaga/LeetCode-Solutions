class Solution:
    def checkDivisibility(self, n: int) -> bool:
        agg, prod = 0, 1
        for dig in str(n):
            agg += int(dig)
            prod *= int(dig)
        
        return n % (agg + prod) == 0