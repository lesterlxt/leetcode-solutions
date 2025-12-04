class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [(-1, -1)] * (n * n + 1)
        label = 1
        left_to_right = True

        for r in range(n - 1, -1, -1):
            if left_to_right:
                cols = range(0, n)
            else:
                cols = range(n - 1, -1, -1)
        
            for c in cols:
                cells[label] = (r,c)
                label += 1
            
            left_to_right = not left_to_right

        q = collections.deque()
        q.append((1, 0))
        visited = {1}

        while q:
            curr, moves = q.popleft()

            if curr == n * n:
                return moves
            
            for step in range(1, 7):
                nxt = curr + step
                if nxt > n * n:
                    break
                
                r, c = cells[nxt]
                if board[r][c] != -1:
                    nxt = board[r][c]
                
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves + 1))
    
        return -1

        
