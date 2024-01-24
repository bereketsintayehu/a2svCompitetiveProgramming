# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()

        lower = dummy1
        higher = dummy2

        while head:
            if head.val < x:
                lower.next = head
                lower = lower.next
            else:
                higher.next = head
                higher = higher.next
            head = head.next

        lower.next = dummy2.next
        higher.next = None

        return dummy1.next