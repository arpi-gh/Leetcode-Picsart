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
        original = head
        dummy = Node(0)
        copy = dummy
        nodes = {}
        while original:
            copy.next = Node(original.val)
            copy = copy.next
            nodes[original] = copy
            original = original.next

        for node in nodes:
            if node.random:
                nodes[node].random = nodes[node.random]

        return dummy.next
