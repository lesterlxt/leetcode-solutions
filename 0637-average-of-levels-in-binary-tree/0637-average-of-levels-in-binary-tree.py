# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_sum = 0
            level_avg = 0
            for i in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_sum += node.val

            level_avg = level_sum / level_size
            res.append(level_avg)
        
        return res



