# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def get_depth(node):
            if not node:
                return 0

            max_left = get_depth(node.left)
            max_right = get_depth(node.right)

            self.max_diameter = max(self.max_diameter, max_left + max_right)
            
            return 1 + max(max_left, max_right)
        
        get_depth(root)
        return self.max_diameter