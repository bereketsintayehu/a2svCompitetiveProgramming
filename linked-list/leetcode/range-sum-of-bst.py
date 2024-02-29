# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def add(root):
            if root:
                if root.val > high:
                    return add(root.left)
                elif root.val < low:
                    return add(root.right)
                else:
                    return add(root.left) + add(root.right) +(root.val if low <= root.val <= high else 0)
                    
            return 0
        
        return add(root)
        