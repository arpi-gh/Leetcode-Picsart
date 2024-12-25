
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Iterative Solution
class Solution:

    def connect(self, root: Node):
        q = [root]
        while q:
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if node:
                    if i < length-1:
                        node.next = q[0]
                    q.append(node.left)
                    q.append(node.right)
        return root

# Recursive Solution

class Solution:
    def connect(self, root: Node, neighbor = None) -> Node:
        if not root:
            return
        root.next = neighbor

        if root.next:
            next_neghbor = root.next.left
        else:
            next_neghbor = None
        self.connect(root.left, neighbor=root.right)
        self.connect(root.right, neighbor=next_neghbor)

        return root
