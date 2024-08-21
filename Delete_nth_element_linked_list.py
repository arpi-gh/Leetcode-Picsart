class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return

        s = head
        f = head
        for i in range(n):
            if f.next is not None:
                f = f.next
            else:
                tmp = head.next
                head.next = None
                return tmp

        while f.next is not None:
            f = f.next
            s = s.next

        s.next = s.next.next
        return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeNthFromEnd(n1, 5))