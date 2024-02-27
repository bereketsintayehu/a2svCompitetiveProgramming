# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(p, q):
            if not (p or q):
                return

            a = p.val if p else 0
            b = q.val if q else 0
            return TreeNode(a + b, merge(p.left if p else None, q.left if q else None), merge(p.right if p else None, q.right if q else None))

        return merge(root1, root2)
            