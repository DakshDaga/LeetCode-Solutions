class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0, c1, c2 = 0, 0, 0
        for stone in stones:
            if stone % 3 == 0: c0 += 1
            elif stone % 3 == 1: c1 += 1
            else: c2 += 1
        
        if c0 % 2 == 0:
            return c1>=1 and c2>=1
        
        return abs(c1-c2) >= 3
            