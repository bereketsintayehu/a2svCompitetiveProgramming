# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        dummy2 = head
        dummy.next = dummy2

        while dummy2:
            curr = dummy2

            while  curr:
                if dummy2.val > curr.val:
                    dummy2.val, curr.val = curr.val, dummy2.val
                curr = curr.next

            dummy2 = dummy2.next

        return dummy.next