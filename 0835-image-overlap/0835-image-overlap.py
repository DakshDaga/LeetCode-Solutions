class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        possible = {}
        n = len(img1)

        def get_diff(i, j):
            for x in range(n):
                for y in range(n):
                    if img2[x][y] == 0: continue
                    row_diff = x-i
                    col_diff = y-j
                    possible[(row_diff, col_diff)] = possible.get((row_diff, col_diff), 0) + 1 

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 0: continue
                get_diff(i, j)
        
        return max(possible.values(), default=0)
