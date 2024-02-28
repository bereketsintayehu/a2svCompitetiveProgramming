# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def findSum(root):
            nonlocal ans
            if root:
                leftSub, leftMin, leftMax = findSum(root.left)
                rightSub, rightMin, rightMax = findSum(root.right)


                left = (leftSub if root.left.val < root.val and leftMax < root.val else -inf) if root.left else 0
                right = (rightSub if root.right.val > root.val and rightMin > root.val else -inf) if root.right else 0

                curMin = min(leftMin, rightMin)
                curMax = max(leftMax, rightMax)

                ans = max(ans, left + right + root.val)

                return (left + right + root.val, min(root.val, curMin), max(root.val, curMax))

            else:
                return (0, inf, -inf)

        findSum(root)
        return ans