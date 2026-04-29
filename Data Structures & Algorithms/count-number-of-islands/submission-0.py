class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS: recursive traversal to explore all connected components
        # BFS: level by level traversal using a queue

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] # down, up, right, left
        num_islands = 0
        def dfs(row, col):
            # check to see if the cell is out of bounds or if the value isn't a valid part of an island 
            # (equals 0)
            if (row >= len(grid) or col >= len(grid[row]) or row < 0 or col < 0 or grid[row][col] == "0"):
                return 
            
            grid[row][col] = "0"
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands

