# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(curMin, curMax, root):
            return (curMin < root.val < curMax) and validate(root.val, curMax, root.right) and validate(curMin, root.val, root.left) if root else True
        
        return validate(-inf, inf, root)