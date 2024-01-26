# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        l = 0

        while curr:
            l += 1
            curr = curr.next
        
        curr = dummy
        i = 0

        while i != l - n:
            curr = curr.next
            i += 1
        
        curr.next = curr.next.next if curr.next else None

        return dummy.next
