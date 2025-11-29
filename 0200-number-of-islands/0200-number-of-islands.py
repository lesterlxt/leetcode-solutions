class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(sr: int, sc: int) -> None:
            q = collections.deque()
            q.append((sr, sc))
            grid[sr][sc] = "0"

            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c+ dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
                    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r,c)
        
        return islands

    

