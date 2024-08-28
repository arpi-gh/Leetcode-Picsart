class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return
        elems = 1
        current = head
        while current.next:
            elems += 1
            current = current.next
        cycles = k // elems
        k -= cycles * elems
        if k == 0:
            return head
        current = prev = head
        for i in range(k):
            current = current.next

        while current.next:
            prev = prev.next
            current = current.next

        new_head = prev.next
        prev.next = None
        current.next = head
        return new_head


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
    print(sol.rotateRight(n1, 5))