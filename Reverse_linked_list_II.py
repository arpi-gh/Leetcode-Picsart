# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head

        at = 1
        current = head
        start = head
        end = head
        while at < left:
            start = current
            current = current.next
            at += 1
        end = current
        nxt = current.next
        at += 1
        while at <= right:
            pivot = nxt
            nxt = nxt.next
            at += 1
            pivot.next = current
            current = pivot
        end.next = nxt
        if left != 1:
            start.next = current
            return head
        return current
