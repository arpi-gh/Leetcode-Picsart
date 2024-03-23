class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}'


def hasCycle(head: ListNode) -> bool:
    if head is None:
        return False
    has_cycle = False
    dummy = ListNode()
    dummy.next = head
    fast = head.next
    slow = dummy
    while fast is not None and fast.next is not None:
        if fast == slow:
            has_cycle = True
            break
        fast = fast.next.next
        slow = slow.next
    return has_cycle


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)

n0 = ListNode()
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n1

print(hasCycle(n1))
