class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        possible = {}
        n = len(img1)
        pos_of_1s_img2 = []

        for x in range(n):
            for y in range(n):
                if img2[x][y] == 1:
                    pos_of_1s_img2.append([x, y])

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 0: continue
                for pos in pos_of_1s_img2:
                    row_diff = i - pos[0]
                    col_diff = j - pos[1]
                    possible[(row_diff, col_diff)] = possible.get((row_diff, col_diff), 0) + 1
        
        return max(possible.values(), default=0)
