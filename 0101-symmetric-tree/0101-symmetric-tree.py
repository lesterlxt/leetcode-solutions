# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            return isMirror(a.left, b.right) and isMirror(a.right, b.left)
        
        if not root:
            return True
        return isMirror(root.left, root.right)