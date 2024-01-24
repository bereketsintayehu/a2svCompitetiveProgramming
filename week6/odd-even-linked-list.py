# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()

        odd = dummy1
        even = dummy2

        i = 1
        curr = head

        while curr:
            if i:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            i ^= 1
            curr = curr.next
        
        odd.next = dummy2.next
        even.next = None
        
        return dummy1.next