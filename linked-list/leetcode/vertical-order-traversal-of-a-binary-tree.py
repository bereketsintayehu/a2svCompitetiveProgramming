# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)

        def trav(root, row, col):
            if root:
                d[col].append((row, root.val))
                trav(root.left, row + 1, col - 1)
                trav(root.right, row + 1, col + 1)
        
        trav(root, 0, 0)

        ans = []
        for col in sorted(d):
            ans.append([val for _, val in sorted(d[col])])

        return ans
        