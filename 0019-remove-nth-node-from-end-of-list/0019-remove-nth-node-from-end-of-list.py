# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        sz = 1
        while curr.next:
            sz += 1
            curr = curr.next
        if sz == n:
            return head.next
        curr = head
        for _ in range(1, sz-n):
            curr = curr.next
        if curr.next and curr.next.next:
            curr.next = curr.next.next
        elif curr.next is None:
            return curr.next
        else:
            curr.next = None
        return head
            
        
        