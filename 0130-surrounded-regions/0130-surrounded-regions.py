class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def mark_safe(sr, sc):
            stack = [(sr,sc)]
            board[sr][sc] = "S"
            while stack:
                r, c = stack.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                        board[nr][nc] = "S"
                        stack.append((nr, nc))

        for r in range(m):
            if board[r][0] == 'O':
                mark_safe(r, 0)
            if board[r][n - 1] == 'O':
                mark_safe(r, n - 1)

        for c in range(n):
            if board[0][c] == 'O':
                mark_safe(0, c)
            if board[m - 1][c] == 'O':
                mark_safe(m - 1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"            
