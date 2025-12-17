class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(row, col, k):
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if board[row][col] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            tmp = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, k + 1) or
                dfs(row - 1, col, k + 1) or
                dfs(row, col + 1, k + 1) or
                dfs(row, col - 1, k + 1)
            )

            board[row][col] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False



