class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def get_area(r, c):
            # Base case: out of bounds or water/visited
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            
            # Mark as visited by sinking the island
            grid[r][c] = 0
            
            # Sum the current cell (1) + all four directions
            return (1 + get_area(r + 1, c) + 
                        get_area(r - 1, c) + 
                        get_area(r, c + 1) + 
                        get_area(r, c - 1))

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, get_area(r, c))

        return max_area