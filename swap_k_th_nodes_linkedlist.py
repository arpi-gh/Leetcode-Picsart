class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow = current = head
        i = 1
        while i < k:
            current = current.next
            i += 1

        fast = current
        while fast.next:
            fast = fast.next
            slow = slow.next

        current.val, slow.val = slow.val, current.val

        return head
