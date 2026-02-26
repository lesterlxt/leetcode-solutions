class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    islands += 1
                    stack = [(row, col)]
                    grid[row][col] = "0"

                    while stack:
                        x, y = stack.pop()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                stack.append((nx, ny))

        return islands