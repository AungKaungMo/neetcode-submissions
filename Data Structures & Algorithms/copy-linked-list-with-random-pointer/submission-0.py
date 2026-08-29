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
        if not head:
            return
        oldCopy = {}

        curr = head
        while curr:
            oldCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                oldCopy[curr].next = oldCopy[curr.next]
            
            if curr.random:
                oldCopy[curr].random = oldCopy[curr.random]

            curr = curr.next
        
        return oldCopy[head]