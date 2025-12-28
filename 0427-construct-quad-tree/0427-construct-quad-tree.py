
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    # pre sum 2d
    def construct(self, grid: List[List[int]]) -> Node:
        n = len(grid)
        pre = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                pre[i+1][j+1] = pre[i][j+1] + row_sum
    
        def area_sum(r, c, size):
            return (pre[r+size][c+size]
            - pre[r][c+size]
            - pre[r+size][c]
            + pre[r][c])
        
        def build(r, c, size):
            total = area_sum(r, c, size)
            if total == 0:
                return Node(False, True, None, None, None, None)
            if total == size * size:
                return Node(True, True, None, None, None, None)

            half = size // 2
            tl = build(r, c, half)
            tr = build(r, c + half, half)
            bl = build(r + half, c, half)
            br = build(r + half, c + half, half)
            return Node(True, False, tl, tr, bl, br)
        
        return build(0, 0, n)
