# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def add(root, curr):
            if root:
                if not (root.left or root.right):
                    return curr * 10 + root.val

                return add(root.left, curr * 10 + root.val) + add(root.right, curr * 10 + root.val)

            return 0
            
        return add(root, 0)