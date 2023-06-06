# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = y = ''
        
        while l1:
            x += str(l1.val)
            l1 = l1.next
        while l2:
            y += str(l2.val)
            l2 = l2.next
        
        lSum = str(int(x[::-1]) + int(y[::-1]))
        lSum = lSum[::-1]
        
        head = ListNode(int(lSum[0]))
        curr = head
        
        for i in range(1, len(lSum)):
            new_node = ListNode(int(lSum[i]))
            curr.next = new_node
            curr = new_node
            
        return head
        
        
        
        