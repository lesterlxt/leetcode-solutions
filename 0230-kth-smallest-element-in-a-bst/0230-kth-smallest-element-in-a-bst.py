# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.visited_cnt = 0
        self.kth_val = None

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            inorder(node.left)

            if self.kth_val is None:
                self.visited_cnt += 1
                if self.visited_cnt == k:
                    self.kth_val = node.val
                    return

            inorder(node.right)
        
        inorder(root)
        return self.kth_val


