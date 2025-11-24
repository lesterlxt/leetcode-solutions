# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def left_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        
        def right_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.right
            return depth
        
        left_h = left_depth(root)
        right_h = right_depth(root)

        if left_h == right_h:
            return (2 ** left_h) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)