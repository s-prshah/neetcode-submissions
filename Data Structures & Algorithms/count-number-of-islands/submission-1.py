class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS: recursive traversal to explore all connected components
        # BFS: level by level traversal using a queue

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] # down, up, right, left
        num_islands = 0
        def bfs(row, col):
            q = deque()
            grid[row][col] = "0"
            q.append((row, col))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr>= len(grid) or nc >= len(grid[row]) or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    num_islands += 1
                    bfs(i, j)
        
        return num_islands

