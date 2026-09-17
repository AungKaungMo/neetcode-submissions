# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        d = deque([(root, float("-inf"), float("inf"))])
        while d:
            node, low, high = d.popleft()

            if not (low < node.val < high):
                return False
            
            if node.left:
                d.append((node.left, low, node.val))
            if node.right:
                d.append((node.right, node.val, high))

        return True


