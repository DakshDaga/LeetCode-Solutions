class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(2)]

        def playForAlice(person, i, M):
            if(i>=n): return 0

            if memo[person][i][M] != -1: return memo[person][i][M]

            stones = 0
            total = -1 if person == 0 else 1e9
            for x in range(1, min(n-i, 2*M) + 1):
                stones += piles[i+x-1]

                if person == 0:
                    total = max(total, stones + playForAlice(1, i+x, max(M, x)))
                else:
                    total = min(total, playForAlice(0, i+x, max(M, x)))
            
            memo[person][i][M] = total
            return memo[person][i][M]

        return playForAlice(0, 0, 1)
        