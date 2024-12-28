# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def connect(self, root: 'Node', parent=None) -> 'Node':
        if not root:
            return
        if parent:
            head = parent
            current = root
            if head.left is current and head.right:
                current.next = head.right
            else:
                head = head.next
                while head:
                    if head.left:
                        current.next = head.left
                        break
                    elif head.right:
                        current.next = head.right
                        break
                    head = head.next

        self.connect(root.right, root)
        self.connect(root.left, root)

        return root


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    # n3.right = n6
    # n5.left = n7
    # n5.right = n8
    # n6.right = n9

    sol = Solution()
    print(sol.connect(n1))
