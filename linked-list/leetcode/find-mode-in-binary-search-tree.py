# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        _max = 0

        def trav(root):
            nonlocal _max
            if root:
                cnt[root.val] += 1
                _max = max(_max, cnt[root.val])
                trav(root.left)
                trav(root.right)
        
        trav(root)

        return [node for node, count in cnt.items() if count == _max]