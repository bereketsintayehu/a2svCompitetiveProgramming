# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def search(node, currMin, currMax):
            if node:
                if node.val < currMin:
                    currMin = node.val
                elif node.val > currMax:
                    currMax = node.val
                search(node.left, currMin, currMax)
                search(node.right, currMin, currMax)
                
            else:
                self.ans = max(self.ans, abs(currMax - currMin))
        
        search(root, root.val, root.val)
        
        return self.ans