# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left_reverted = self.invertTree(root.left)
        right_reverted = self.invertTree(root.right)
        root.left, root.right = right_reverted, left_reverted

        return root