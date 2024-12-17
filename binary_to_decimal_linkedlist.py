class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head.next:
            if head.val == 1:
                return 1
            else:
                return 0

        current = head
        next_node = head.next
        current.next = None

        while next_node:
            pivot = next_node
            next_node = next_node.next
            pivot.next = current
            current = pivot

        power = 0
        res = 0
        while current:
            if current.val:
                res += 2 ** power
            current = current.next
            power += 1

        return res


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(0)
    n3 = ListNode(1)

    n1.next = n2
    n2.next = n3

    sol = Solution()
    print(sol.getDecimalValue(n1))