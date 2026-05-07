class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1. check for 1
        2. count++ if 1 is found
        3. keep track of visited
        """
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] == "0":
                return 

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
    
        return islands
