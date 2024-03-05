# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def trav(root):
            if root:
                trav(root.left)
                vals.append(root.val)
                trav(root.right)
        
        trav(root)
        def balance(l, r):
            if l <= r:
                m = (l + r) // 2
                return TreeNode(vals[m], balance(l, m - 1), balance(m + 1, r))

        return balance(0, len(vals) - 1)