class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        
        memo = {}
        def solve(i, j, count):
            if i==m-1 and j==n-1:
                if count == 1: return True
                return False
            
            if i>=m or j>=n or count<0:
                return False

            if grid[i][j] == '(':
                count += 1
            else: count -= 1
            if (i, j, count) in memo: return memo[(i, j, count)]

            go_right = solve(i, j+1, count)
            go_down = solve(i+1, j, count)

            memo[(i, j, count)] = go_right or go_down
            return go_right or go_down
        
        return solve(0, 0, 0)