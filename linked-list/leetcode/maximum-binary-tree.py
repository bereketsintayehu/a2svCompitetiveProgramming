# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def cons(l, r):
            if l < r:
                mx = max(nums[l:r])
                indx = nums.index(mx)
                return TreeNode(mx, cons(l, indx), cons(indx + 1, r))
        
        return cons(0, len(nums))