class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        
        rows, cols = len(board), len(board[0])
        
        def bfs(start_row: int, start_col: int) -> None:
            q = collections.deque()
            q.append((start_row, start_col))
            board[start_row][start_col] = "T"

            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        board[nr][nc] == "O"):
                        board[nr][nc] = "T"
                        q.append((nr, nc))
        
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)
            
        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        
                
