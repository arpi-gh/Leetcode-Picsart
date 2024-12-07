class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        next_node = head.next
        current = head
        head.next = None
        while next_node:
            pivot = next_node
            next_node = next_node.next
            pivot.next = current
            current = pivot
        head = current
        return head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    sol = Solution()
    print(sol.reverseList(n1))