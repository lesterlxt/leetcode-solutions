# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        flag = 1
        
        while q:
            level_size = len(q)
            level_nodes = []

            for i in range(level_size):
                node = q.popleft()
                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if flag == 1:
                res.append(level_nodes)
            else:
                res.append(level_nodes[::-1])
            flag *= -1
            
        return res
            
            

            

