class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head.next:
            return True

        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            head2 = slow.next.next
            fast = fast.next
        else:
            head2 = slow.next

        slow.next = None
        current = head2
        next_node = current.next
        current.next = None

        while next_node:
            pivot = next_node
            next_node = next_node.next
            pivot.next = current
            current = pivot

        left = head
        right = fast

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


if __name__ == '__main__':
    values = [1, 0, 3, 4, 0, 1]

    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)

    sol = Solution()
    print(sol.isPalindrome(linked_list.head))
