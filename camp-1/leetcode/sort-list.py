# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(p, q):
            dummy = ListNode()
            cur = dummy

            while p and q:
                if p.val < q.val:
                    cur.next = p
                    p = p.next
                else:
                    cur.next = q
                    q = q.next
                cur = cur.next
            
            cur.next = p or q

            return dummy.next
        
        def mergeSort(ls):
            if (not ls) or (not ls.next):
                return ls

            slow, fast = ls, ls.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            mid = slow.next
            slow.next = None

            return merge(mergeSort(ls), mergeSort(mid))
        
        return mergeSort(head)