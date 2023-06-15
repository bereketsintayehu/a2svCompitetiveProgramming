# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevelSum = root.val
        maxLevel = 1
        queue = [(root, 1)]  

        while queue:
            levelSum = 0
            levelSize = len(queue)

            for _ in range(levelSize):
                node, level = queue.pop(0)
                levelSum += node.val

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                maxLevel = level

        return maxLevel