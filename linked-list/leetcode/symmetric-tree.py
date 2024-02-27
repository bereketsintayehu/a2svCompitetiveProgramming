# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p, q):
            if p and q:
                if p.val != q.val:
                    return False

                return (check(p.left, q.right) and check(p.right, q.left))

            elif p or q:
                return False
            
            return True

        return check(root.left, root.right)