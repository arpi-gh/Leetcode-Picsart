class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current = list1
        i = 1
        while i < a:
            current = current.next
            i += 1

        suffix = current.next
        current.next = list2
        while current.next:
            current = current.next

        while i <= b:
            suffix = suffix.next
            i += 1
        current.next = suffix

        return list1


