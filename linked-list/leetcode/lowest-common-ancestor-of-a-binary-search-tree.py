# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root):
            if root:
                if min(p.val, q.val) <= root.val <= max(q.val, p.val):
                    return root

                elif min(p.val, q.val) > root.val:
                    return find(root.right)
                    
                else:
                    return find(root.left)


        return find(root)