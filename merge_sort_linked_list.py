class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        elif head.next.next is None:
            head_left = head
            head_right = head.next
            head.next = None
        else:
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            head_left = head
            head_right = slow.next
            slow.next = None

        left = Solution.sortList(self, head_left)
        right = Solution.sortList(self, head_right)

        return Solution.merge(self, left, right)

    def merge(self, head1, head2):
        dummy = ListNode(0)
        current = head1
        compared = head2
        pointer = dummy
        while current:
            if compared:
                if current.val <= compared.val:
                    pointer.next = current
                else:
                    pointer.next = compared
                    current, compared = compared, current
            else:
                pointer.next = current
            current = current.next
            pointer = pointer.next
        if compared:
            pointer.next = compared
        return dummy.next


# n1 = ListNode(1)
# n2 = ListNode(2)
# n4 = ListNode(4)
# n1.next = n2
# n2.next = n4
#
# m1 = ListNode(1)
# m3 = ListNode(3)
# m4 = ListNode(4)
#
# m1.next = m3
# m3.next = m4
#
# ls1 = n1
# ls2 = m1

n1 = ListNode(0)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(6)
n5 = ListNode(2)
n6 = ListNode(-1)
n7 = ListNode(8)
n8 = ListNode(-2)
n9 = ListNode(7)
n10 = ListNode(1)
n11 = ListNode(3)
n12 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11
n11.next = n12

print(sortList(n1))
current = n1
while current:
    print(current)
    current = current.next
