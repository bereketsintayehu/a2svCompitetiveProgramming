# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def BFS(root):
            nonlocal ans
            if root:
                queue = deque([(root, 0)])
                prev = 0
                cur = []

                while queue:
                    root, h = queue.popleft()
                    if h > prev:
                        if prev % 2:
                            ans.append(cur[::-1])
                        else:
                            ans.append(cur)
                        prev = h
                        cur = []

                    cur.append(root.val)
                    if root.left:
                        queue.append((root.left, h + 1))
                   
                    if root.right:
                        queue.append((root.right, h + 1))
                if cur:
                    if prev % 2:
                        ans.append(cur[::-1])
                    else:
                        ans.append(cur)

        BFS(root)
        return ans