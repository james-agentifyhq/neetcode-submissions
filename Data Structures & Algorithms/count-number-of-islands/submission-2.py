class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        approach: dfs, remember
        expected: count
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
        VISITED = "0"
        def dfs(row, col):
            if 0 > row or row >= ROWS or 0 > col or col >= COLS or grid[row][col] == "0":
                return
            grid[row][col] = VISITED
            for dr, dc in DIRECTIONS:
                dfs(row + dr, col + dc)


        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    continue                    
                dfs(r, c)
                islands += 1

        return islands