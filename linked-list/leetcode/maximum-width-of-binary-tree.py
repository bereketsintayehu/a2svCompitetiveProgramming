# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque([(root, 0, 0)])
        cur = []
        pre = 0

        while queue:
            root, val, d = queue.popleft()

            if d > pre:
                pre = d
                ans = max(ans, cur[-1] - cur[0] + 1)
                cur = []

            cur.append(val)

            if root.left:
                queue.append((root.left, val * 2, d + 1))
            if root.right:
                queue.append((root.right, val * 2 + 1, d + 1))

        if cur:
            ans = max(ans, cur[-1] - cur[0] + 1)

        return ans