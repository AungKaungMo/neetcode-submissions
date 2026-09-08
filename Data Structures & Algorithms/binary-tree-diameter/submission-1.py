# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        
        max_diameter = 0
        stack = [root]
        depth = {}
        while stack:
            curr = stack[-1]

            if curr.left and curr.left not in depth:
                stack.append(curr.left)
            elif curr.right and curr.right not in depth:
                stack.append(curr.right)
            else:
                val = stack.pop()

                left_max = depth.get(curr.left, 0)
                right_max = depth.get(curr.right, 0)
                
                max_diameter = max(max_diameter, left_max + right_max)
                depth[val] = 1 + max(left_max, right_max)
        return max_diameter


