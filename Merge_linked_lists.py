class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def mergeTwoLists(list1: ListNode, list2: ListNode) -> [ListNode]:
    dummy = ListNode(0)
    current = list1
    compared = list2
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



n1 = ListNode(1)
n2 = ListNode(2)
n4 = ListNode(4)
n1.next = n2
n2.next = n4

m1 = ListNode(1)
m3 = ListNode(3)
m4 = ListNode(4)

m1.next = m3
m3.next = m4

ls1 = n1
ls2 = m1


print(mergeTwoLists(ListNode(0), ListNode(0)))