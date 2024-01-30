# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        vals = []
        i = 1
        curr = head

        while curr:
            if i == left:
                while i <= right:
                    vals.append(curr.val)
                    curr = curr.next
                    i += 1
                break
            curr = curr.next
            i += 1

        vals = vals[::-1]
        
        i = 1
        curr = head
        while curr:
            if i == left:
                while i <= right:
                    curr.val = vals[i - left]
                    curr = curr.next
                    i += 1
                break
            i += 1
            curr = curr.next

        return head