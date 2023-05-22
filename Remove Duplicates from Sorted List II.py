# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        j = head.next
        
        while j.next != None:
            while j.val == j.next.val:
                j = j.next
                i.next = j.next
                
            i = j
            j = j.next
        
        return head
