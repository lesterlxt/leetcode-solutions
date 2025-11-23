# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_again = max(dfs(node.left), 0)
            right_again = max(dfs(node.right), 0)

            current_path = node.val + left_again + right_again
            self.max_sum = max(current_path, self.max_sum)

            return node.val + max(left_again, right_again)
        
        dfs(root)
        return self.max_sum
