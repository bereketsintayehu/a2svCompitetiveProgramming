# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        ans = []
        node = deque()
        index = deque()
        i = 0
        while head:
            vals.append(head.val)
            ans.append(0)
            
            while node and node[-1] < head.val:
                ans[index.pop()] = head.val
                node.pop()
            
            node.append(head.val)
            index.append(i)
            i += 1
            head = head.next
        
        return ans
            
                
        