"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            nxt = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = nxt
            cur = nxt
        
        cur = head
        while cur:
            copy = cur.next
            copy.random = cur.random.next if cur.random else None
            cur = copy.next
        
        dummy = Node(0)
        copy_cur = dummy
        cur = head

        while cur:
            copy = cur.next
            nxt = copy.next

            copy_cur.next = copy
            copy_cur = copy

            cur.next = nxt
            cur = nxt
        
        return dummy.next

