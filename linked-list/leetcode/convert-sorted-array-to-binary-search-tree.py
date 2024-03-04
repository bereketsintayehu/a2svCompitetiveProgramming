# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def trav(l, r):
            if l <= r:
                m = (l + r) // 2
                return TreeNode(nums[m], trav(l, m - 1), trav(m + 1, r))
        
        return trav(0, len(nums) - 1)