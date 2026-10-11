class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxA = 0

        #iterate thru grid
        #use dfs when encountering a 1
        #update max area
        def dfs(i, j):
            if (i < 0 or i >= ROWS
            or j < 0 or j >= COLS
            or grid[i][j] == 0):
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxA = max(maxA, area)
        return maxA

