# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy, big_dummy = ListNode(), ListNode()
        small, big = small_dummy, big_dummy

        cur = head
        while cur:
            nxt = cur.next
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            cur.next = None
            cur = nxt
        
        small.next = big_dummy.next
        return small_dummy.next