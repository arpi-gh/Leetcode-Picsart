# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = last_even = head.next
        next_odd = even.next
        next_even = next_odd.next

        while next_odd:
            odd.next = next_odd
            next_odd.next = even
            last_even.next = next_even

            if not next_even:
                break
            next_odd = next_even.next

            if not next_odd:
                break

            last_even = next_even
            next_even = next_odd.next

            odd = odd.next

        return head