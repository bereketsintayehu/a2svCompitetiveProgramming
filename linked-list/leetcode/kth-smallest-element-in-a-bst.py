# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        def trav(root):
            if root:
                trav(root.left)
                s.append(root.val)
                trav(root.right)
        trav(root)
        return s[k - 1]