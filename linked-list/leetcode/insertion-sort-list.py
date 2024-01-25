# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head

        while head:
            curr = head

            while  curr:
                if head.val > curr.val:
                    head.val, curr.val = curr.val, head.val
                curr = curr.next

            head = head.next

        return dummy.next