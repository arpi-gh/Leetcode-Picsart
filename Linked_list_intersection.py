class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        a = headA
        b = headB
        reached_end = 0

        while a is not b:
            if not a.next and not b.next:
                return None

            if not a.next:
                if reached_end == 2:
                    return None
                a = headB
                b = b.next
                reached_end += 1

            elif not b.next:
                if reached_end == 2:
                    return None
                b = headA
                a = a.next
                reached_end += 1

            else:
                a = a.next
                b = b.next

        return a


if __name__ == '__main__':
    a1 = ListNode(4)
    a2 = ListNode(1)
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)

    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)

    a1.next = a2
    a2.next = c1
    b1.next = b2
    b2.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2
    c2.next = c3


sol = Solution()
print(sol.getIntersectionNode(a1, b1))
